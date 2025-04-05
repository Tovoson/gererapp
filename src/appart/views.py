from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import DetailsAppart
from .serializers import DetailsSerializer

class AppartementViewSet(viewsets.ModelViewSet):
    queryset = DetailsAppart.objects.all()
    serializer_class = DetailsSerializer
    permission_classes = [AllowAny]
    
    # Si vous avez besoin de logique personnalisée lors de la création
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
        