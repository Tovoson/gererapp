
from rest_framework import viewsets, status
from appart.models import DetailsAppart
from appart.serializers import AjouterAppartementSerializer, DetailsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class AppartViewSet(viewsets.ModelViewSet):
    queryset = DetailsAppart.objects.all()
    serializer_class = DetailsSerializer
    
class AjouterAppartView(APIView):
    queryset = DetailsAppart.objects.all()
    serializer_class = AjouterAppartementSerializer
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            numapp = serializer.validated_data["numapp"]
            
            if self.queryset.filter(pk=numapp).exists():
                return Response("Numapp existe déjà", status=400)
            else:
                appart = serializer.save()
                return Response(DetailsSerializer(appart).data, status=201)
        else:
            return Response(serializer.errors, status=400)
        