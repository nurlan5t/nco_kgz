from rest_framework.views import APIView
from info.models import News, TypeLaw, Law, Publication
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from info.serializers import NewsSerializer, NewsDetailSerializer, LawTypesSerializer, LawsSerializer, PublicationTypeSerializer


class NewsCreateAPI(APIView, PageNumberPagination):
    def get(self, request):
        search_word = request.query_params.get('search_word', '')
        news = News.objects.filter(Q(title__icontains=search_word) | Q(text__icontains=search_word))
        results = self.paginate_queryset(news, request, view=self)
        return self.get_paginated_response(NewsSerializer(results, many=True).data)

class NewsDetailApi(APIView):
    def get(self, request, id):
        news = News.objects.get(pk=id)
        data = NewsDetailSerializer(news).data
        return Response(data=data)

class LawTypesAPI(APIView):
    def get(self, request):
        law_types = TypeLaw.objects.all()
        data = LawTypesSerializer(law_types, many=True).data
        return Response(data=data)

class LawTypeAPI(APIView):
    def get(self, request, pk):
        law_type = Law.objects.filter(law_type=pk)
        data = LawsSerializer(law_type, many=True).data
        return Response(data=data)

class LawDetailAPI(APIView):
    def get(self, request, id):
        news = Law.objects.get(pk=id)
        data = LawsSerializer(news).data
        return Response(data=data)

class PublicationTypeAPI(APIView):
    def get(self, request, pk):
        types = Publication.objects.filter(types=pk)
        data = PublicationTypeSerializer(types, many=True).data
        return Response(data=data)

class PublicationDetailAPI(APIView):
    def get(self, request, pk):
        publication = Publication.objects.get(pk=pk)
        data = PublicationTypeSerializer(publication).data
        return Response(data=data)