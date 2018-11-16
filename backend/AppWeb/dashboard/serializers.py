from rest_framework import serializers

from . import models


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Page
        fields = ('page_id','name')