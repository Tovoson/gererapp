
from rest_framework import viewsets
from appart.models import DetailsAppart
from appart.serializers import DetailsSerializer


class AppartViewSet(viewsets.ModelViewSet):
    queryset = DetailsAppart.objects.all()
    serializer_class = DetailsSerializer
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # type: ignore
           
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # type: ignore
        
    def retrieve(self, request, pk=None):
        material = self.queryset.get(pk=pk)
        serializer = self.serializer_class(material)
        return Response(serializer.data) # type: ignore