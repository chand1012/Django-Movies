import requests
import os

IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={key}' 
KEY = os.getenv('MOVIE_DB_KEY')

def get_movie_poster_url(imdb_id):
    url = IMG_PATTERN.format(imdbid=imdb_id, key=KEY)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get('posters'):
            path = data['posters'][0]['file_path']
            return f'https://image.tmdb.org/t/p/original{path}'
