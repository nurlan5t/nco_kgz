from rest_framework.views import APIView
from info.models import News
from rest_framework.response import Response
from info.serializers import NewsSerializer


class NewsCreateAPI(APIView):
    def get(self, request):
        news = News.objects.all()
        data = NewsSerializer(news, many=True).data
        return Response(data=data)

