import requests
api_key= "d8d666fb30f19051784ac3645fdf05da"
base_url= "https://api.themoviedb.org/3"


def search_person(name):
    url = f"{base_url}/search/person"
    params = {
        "api_key": api_key,
        'query':name
        }
    response= requests.get(url,params=params)
    return response.json()

def search_person_id(person_id):
    url= f"{base_url}/person/{person_id}"
    params={
        "api_key": api_key,
    }
    
    response= requests.get(url,params=params)
    return response.json()


def filmography(person_id):
    url = f"{base_url}/person/{person_id}/movie_credits"
    params = {"api_key": api_key}

    data = requests.get(url, params=params).json()

    HORROR_GENRE_ID = 27

    # Filter langsung
    data["cast"] = [
        f for f in data.get("cast", [])
        if HORROR_GENRE_ID in f.get("genre_ids", [])
    ]

    data["crew"] = [
        f for f in data.get("crew", [])
        if HORROR_GENRE_ID in f.get("genre_ids", [])
    ]

    return data

