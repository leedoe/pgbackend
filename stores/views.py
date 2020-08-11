from config.settings.base import env
from django.http.response import JsonResponse
from django.views.generic.base import View

import requests

# Create your views here.


class AddressFromNaver(View):
    def get(self, request):
        NAVER_API_KEY_ID = env("NAVER_API_KEY_ID", default="",)
        NAVER_API_KEY = env("NAVER_API_KEY", default="",)

        query = request.GET.get('query', None)

        response = requests.get(
            'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode',
            headers={
                'X-NCP-APIGW-API-KEY-ID': NAVER_API_KEY_ID,
                'X-NCP-APIGW-API-KEY': NAVER_API_KEY
            },
            params={
                'query': query
            }
        )

        return JsonResponse(response.json())
