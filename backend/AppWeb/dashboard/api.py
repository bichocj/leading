from rest_framework import viewsets
from . import serializers, models


class PageViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PageSerializer
    queryset = models.Page.objects.all()

    def perform_create(self, serializer):
    	serializer.save(owner=self.request.user)