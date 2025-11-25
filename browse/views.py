import requests
from django.shortcuts import render
from .models import Movie



def index(request):
    movies = Movie.objects.all()
   
    
    name = request.GET.get("name")
    lang = request.GET.get("lang")
    rating = request.GET.get("rating")
    year = request.GET.get("year")
    
    if name:
        movies = movies.filter(title__icontains=name)
    if lang:
        movies = movies.filter(language=lang)
    if rating:
        try:
            movies = movies.filter(vote_average__gte=float(rating))
        except ValueError:
            pass
    if year:
        if '-' in year:
            start, end = year.split('-')
            try:
                movies = movies.filter(release_year__gte=int(start), release_year__lte=int(end))
            except ValueError:
                pass
        else:
            try:
                movies = movies.filter(release_year=int(year))
            except ValueError:
                pass

    # # Ambil poster dari TMDB
    # movies_with_posters = []
    # for movie in movies:
    #     poster_url = ""
    #     try:
    #         url = f"https://api.themoviedb.org/3/movie/{movie.tmdb_id}"
    #         params = {"api_key": "d8d666fb30f19051784ac3645fdf05da"}
    #         resp = requests.get(url, params=params).json()
    #         poster_path = resp.get("poster_path")
    #         if poster_path:
    #             poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
    #     except requests.exceptions.RequestException as e:
    #         print(f"Error fetching poster for {movie.title}: {e}")
    #     movies_with_posters.append({
    #         "title": movie.title,
    #         "release_year": movie.release_year,
    #         "vote_average": movie.vote_average,
    #         "language": movie.language,
    #         "poster_url": poster_url
    #     })

    languages = [
        { "code": "en", "name": "English" },
        { "code": "ja", "name": "Japanese" },
        { "code": "ko", "name": "Korean" },
        { "code": "es", "name": "Spanish" },
        { "code": "fr", "name": "French" },
        { "code": "zh", "name": "Chinese (Mandarin)" },
        { "code": "th", "name": "Thai" },
        { "code": "id", "name": "Indonesian" },
        { "code": "hi", "name": "Hindi" },
        { "code": "ru", "name": "Russian" },
        { "code": "pt", "name": "Portuguese" },
        { "code": "it", "name": "Italian" },
        { "code": "de", "name": "German" },
        { "code": "tr", "name": "Turkish" },
        { "code": "ph", "name": "Filipino (Tagalog)" }
    ]
    
    # movies_with_posters=movies_with_posters[:10]

    return render(request, "browse/index.html", {"languages": languages})
