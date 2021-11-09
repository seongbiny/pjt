import requests
from tmdb import TMDBHelper


def popular_count():
    """
    popular 영화목록의 개수 출력.
    """
    pass
    tmdb_helper = TMDBHelper('key')
    url = tmdb_helper.get_request_url(region='KR', language='ko')

    data = requests.get(url).json()
    popular_movies = data['results']
    #print(url)

    return len(popular_movies)


if __name__ == '__main__':
    print(popular_count())
