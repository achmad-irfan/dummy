import requests
from datetime import datetime, timedelta
from django.shortcuts import render

def get_upcoming_movies():
    url= 'https://api.themoviedb.org/3/discover/movie'
    release_date = (datetime.today() + timedelta(days=30)).strftime('%Y-%m-%d')
    params = {
        "api_key": "d8d666fb30f19051784ac3645fdf05da",
        "with_genres": "27",
        "primary_release_date.gte": release_date,
        "sort_by": "primary_release_date.asc",
        "language": "en-US"
  }
    
    
    response= requests.get(url,params=params)
    return response.json().get('results',[])


def top_rating():
    url= 'https://api.themoviedb.org/3/discover/movie'
    params = {
        "api_key": "d8d666fb30f19051784ac3645fdf05da",
        "with_genres": "27",
        "sort_by": "vote_average.desc",
        "vote_count.gte": 100, 
    }
    
    response= requests.get(url,params=params)
    return response.json().get('results',[])