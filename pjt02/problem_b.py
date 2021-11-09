import requests
from tmdb import TMDBHelper
from pprint import pprint


def vote_average_movies():
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 출력.
    """
    pass
    list = []
    tmdb_helper = TMDBHelper('key')
    url = tmdb_helper.get_request_url(region='KR', language='ko')

    data = requests.get(url).json()
    popular_movies = data['results']
    for i in popular_movies:
        if i['vote_average'] >= 8:
            list.append(i)
    return list



if __name__ == '__main__':
    pprint(vote_average_movies())
