from django.shortcuts import render
from django.views.generic import TemplateView
from browse.models import Movie
from django.db.models import Count, Avg
from .utils import fig_to_base64
import matplotlib.pyplot as plt

SUBTITLE = (
    "Explore key insights into horror films, including ratings, release trends, "
    "and popularity—presented through clear, data-driven visuals."
)

class Analyst(TemplateView):
    template_name = 'analyst/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = SUBTITLE

        # ================================
        # 1. Grafik: Movie Per Year
        # ================================
        data_year = (
            Movie.objects.values("release_year")
            .exclude(release_year__in =[2025,2026])
            .annotate(total=Count("id"))
            .order_by("release_year")
        )
        years = [d["release_year"] for d in data_year]
        totals = [d["total"] for d in data_year]

        fig1, ax1 = plt.subplots()
        ax1.plot(years, totals)
        ax1.set_title("Horror Movies per Year")
        ax1.set_xlabel("Year")
        ax1.set_ylabel("Movie Count")
        fig1.patch.set_facecolor("#222222")
        ax1.set_facecolor("#333333")
        ax1.tick_params(colors="white")
        ax1.title.set_color("white")
        ax1.tick_params(colors="white")
        ax1.spines["bottom"].set_color("white")
        ax1.spines["left"].set_color("white")

        graph1 = fig_to_base64(fig1)
        context["graph1"] = graph1

        # ================================
        # 2. Grafik: Top Rated Movies (vote > 500)
        # ================================
        top_rated = (
            Movie.objects.filter(vote_count__gte=500)
            .order_by("-vote_average")[:10]
        )

        titles = [m.title[:15] + "..." for m in top_rated]  # biar pendek
        ratings = [m.vote_average for m in top_rated]

        fig2, ax2 = plt.subplots()
        ax2.barh(titles, ratings)
        ax2.set_xlim(7.7, 8.5)
        ax2.set_title("Top 10 Highest Rated Horror Movies (Votes > 500)")
        ax2.title.set_color("white")
        ax2.invert_yaxis()
        ax2.tick_params(colors="white")
        ax2.tick_params(colors="white")
        graph2 = fig_to_base64(fig2)
        context["graph2"] = graph2

        # ================================
        # 3. Grafik: Indonesia Movie Horror 
        # ================================
        data_year_indonesia = (
            Movie.objects.values("release_year")
            .filter(language="id")
            .exclude(release_year__in =[2025,2026])
            .annotate(total=Count("tmdb_id"))
            .order_by("release_year")
        )
        years = [d["release_year"] for d in data_year_indonesia]
        totals = [d["total"] for d in data_year_indonesia]

        fig3, ax3 = plt.subplots()
        ax3.plot(years, totals)
        ax3.set_title("Indonesia Movie Horror")
        ax3.set_xlabel("Year")
        ax3.set_ylabel("Movie Count")
        fig3.patch.set_facecolor("#222222")
        ax3.set_facecolor("#333333")
        ax3.set_xlim(1970, 2024)
        ax3.tick_params(colors="white")
        ax3.title.set_color("white")
        ax3.tick_params(colors="white")
        ax3.spines["bottom"].set_color("white")
        ax3.spines["left"].set_color("white")

        graph3 = fig_to_base64(fig3)
        context["graph3"] = graph3

        # ================================
        # 4. Grafik: 
        # Popular vs Vote_average
        # 
        # ================================
        top_movies = (
            Movie.objects
            .filter(vote_count__gte=1000, popularity__lte=11)
            .exclude(popularity=None)             
            .exclude(vote_average=None)        
            .order_by("-popularity")[:50])

        popularities = [m.popularity for m in top_movies]
        ratings = [m.vote_average for m in top_movies]
        
        fig4, ax4 = plt.subplots(figsize=(7,5))

        ax4.scatter(popularities, ratings, alpha=0.7)

        ax4.set_title("Popularity vs Vote Average (Top 1000 Most Popular Movies)")
        ax4.set_xlabel("Popularity")
        ax4.set_ylabel("Vote Average (0–10)")

        # background gelap elegan
        fig4.patch.set_facecolor("#222222")
        ax4.set_facecolor("#333333")

        # warna tulisan
        ax4.tick_params(colors="white")
        ax4.title.set_color("white")
        ax4.xaxis.label.set_color("white")
        ax4.yaxis.label.set_color("white")

        # biar title dan plot tidak kepotong
        plt.tight_layout()

        # convert ke base64 jika untuk Django
        graph4 = fig_to_base64(fig4)
        context["graph4"] = graph4


        return context
