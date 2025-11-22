from django.shortcuts import render
from . import api
from datetime import datetime

# Create your views here.
def index(request):
    upcoming_movies = api.get_upcoming_movies()
    top_movies = api.top_rating()
    years = range(1980, 2026)

    selected_year = request.GET.get("year")

    # Sort & slicing
    upcoming_movies = sorted(
        upcoming_movies,
        key=lambda m: datetime.strptime(m.get("release_date", "2100-01-01"), "%Y-%m-%d")
    )
    

    # Default empty list agar tidak error
    best_movies = []

    # Filter by year jika dipilih
    if selected_year:
        best_movies = [
            m for m in top_movies
            if m.get("release_date", "").startswith(str(selected_year))
        ]
    
    upcoming_movies = upcoming_movies[:5]
    top_movies = top_movies[:6]

    context = {
        'upcoming_movies': upcoming_movies,
        'top_movies': top_movies,
        'best_movies': best_movies,
        'years': years,
    }
    return render(request,'index.html', context)



def detail_movie(request, slug):
    upcoming_movies = api.get_upcoming_movies()
    top_movies = api.top_rating()
    
    
    for movie in upcoming_movies + top_movies:
        if 'slug' not in movie:
            movie['slug'] = slugify(movie['title'])
    
    
    all_movies = upcoming_movies + top_movies
    
   
    movie = next((m for m in all_movies if m['slug'] == slug), None)
    
    if not movie:
        return render(request, "404.html")  
    
    context = {
        'movie': movie
    }
    return render(request, 'detail_movie.html', context)
