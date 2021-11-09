import requests

class TMDBHelper:
    """API 요청에 필요한 기능들을 제공합니다.

    Attributes:
        api_key: API 서비스에서 발급받은 API KEY입니다.
    """

    def __init__(self, api_key=None):
        self.api_key = api_key


    def get_request_url(self, method='/movie/popular', **kwargs):
        """API 요청에 필요한 주소를 구성합니다.
        
        Args:
            method: API 서비스에서 제공하는 메서드로써 기본 경로 뒤에 추가됩니다.
            **kwargs: 쿼리 스트링 형태로 기본 요청 주소 뒤에 추가됩니다.

        Returns:
            base_url, 메서드, 쿼리 스트링으로 구성된 요청 주소를 반환합니다.
        """
        base_url = 'https://api.themoviedb.org/3'
        request_url = base_url + method
        request_url += f'?api_key={self.api_key}'

        for k, v in kwargs.items():
            request_url += f'&{k}={v}'

        return request_url
    

    def get_movie_id(self, title):
        """영화 제목을 이용하여 아이디를 추출합니다.

        영화 제목을 이용하여 TMDB API 서버에 요청을 보내고 
        응답 결과에서 해당 영화의 id 값을 반환합니다.

        Args:
            title: 영화 제목.
        
        Returns:
            영화 아이디(id)를 반환합니다.
            단, 응답 결과가 없을 경우 None을 반환합니다.
        """
        request_url = self.get_request_url('/search/movie', query=title, region='KR', language='ko')
        data = requests.get(request_url).json()
        results = data.get('results')
        if results:
            movie = results[0]
            movie_id = movie['id']
            return movie_id
        else:
            return None


