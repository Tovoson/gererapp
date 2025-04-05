from rest_framework import routers, serializers, viewsets
from appart.models import DetailsAppart


class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailsAppart
        fields = ['id', 'design', 'loyer']
        
# class AjouterAppartementSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DetailsAppart
#         fields = ['numapp', 'design', 'loyer']
    
# class ModifierSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DetailsAppart
#         fields = ['numapp', 'design', 'loyer']