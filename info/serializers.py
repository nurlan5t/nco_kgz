from rest_framework import serializers

from info.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = 'id title text created'.split()