import requests
from tmdb import TMDBHelper
from pprint import pprint
from operator import itemgetter


def ranking():
    """
    popular 영화목록을 정렬하여 평점순으로 5개 출력.
    """
    pass
    result = []
    tmdb_helper = TMDBHelper('key')
    url = tmdb_helper.get_request_url(region='KR', language='ko')

    data = requests.get(url).json()
    popular_movies = data['results']
    list = sorted(popular_movies, key=itemgetter('vote_average'), reverse=True)
    for i in range(5):
        result.append(list[i])
    return result
    
     


if __name__ == '__main__':
    pprint(ranking())

