from rest_framework import serializers

from info.models import News, NewsImage, TypeLaw, Law, Publication


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = 'id title short_text created image'.split()


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = 'id image'.split()


class NewsDetailSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model = News
        fields = 'id title text created link images'.split()

class LawTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeLaw
        fields = 'id name'.split()

class LawsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Law
        fields = 'id title text law_type'.split()

class PublicationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = 'id title text types file'.split()