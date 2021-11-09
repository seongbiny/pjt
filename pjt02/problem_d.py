import requests
from tmdb import TMDBHelper
from pprint import pprint


def recommendation(title):
    """
    제목에 해당하는 영화가 있으면
    해당 영화의 id를 기반으로 추천 영화 목록을 출력.
    추천 영화가 없을 경우 [] 출력.
    영화 id검색에 실패할 경우 None 출력.
    """
    pass
    tmdb_helper = TMDBHelper('key')
    movie_id = tmdb_helper.get_movie_id(title)
    url = tmdb_helper.get_request_url(f'/movie/{movie_id}/recommendations',language='ko', page=1)
    data = requests.get(url).json()
    list = []
    
    if movie_id == None:
        return None
        
    for i in range(len(data['results'])):
        reco = data['results'][i]['title']
        #print(reco)
        list.append(reco)
    return list
    
    
        

    


if __name__ == '__main__':
    pprint(recommendation('기생충'))
    pprint(recommendation('그래비티'))
    pprint(recommendation('검색할 수 없는 영화'))
