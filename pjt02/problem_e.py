import requests
from tmdb import TMDBHelper
from pprint import pprint


def credits(title):
    """
    제목에 해당하는 영화가 있으면
    해당 영화 id를 통해 영화 상세정보를 검색하여
    주연배우 목록과 목록을 출력.
    영화 id검색에 실패할 경우 None 출력.
    """
    pass

    ca = []
    cr = []

    tmdb_helper = TMDBHelper('key')
    movie_id = tmdb_helper.get_movie_id(title)
    url = tmdb_helper.get_request_url(f'/movie/{movie_id}/credits',language='ko')
    data = requests.get(url).json()
    
    if movie_id == None:
        return None
    
    for i in range(len(data['cast'])):
        if data['cast'][i]['cast_id'] < 10:
            c1 = data['cast'][i]['name']
            ca.append(c1)
    for i in range(len(data['crew'])):
        if data['crew'][i]['department'] == 'Directing':
            c2 = data['crew'][i]['name']
            cr.append(c2)
    
        result = {'cast':ca, 'crew':cr}
    return result
    





if __name__ == '__main__':
    pprint(credits('기생충'))
    pprint(credits('검색할 수 없는 영화'))
