from rest_framework import routers, serializers, viewsets
from appart.models import DetailsAppart


class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailsAppart
        fields = ['numapp', 'design', 'loyer']