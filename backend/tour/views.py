from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Destination
from .serializers import DestinationSerializer

class DestinationListView(APIView):
    def get(self, request):
        destinations = Destination.objects.all()
        serializer = DestinationSerializer(destinations, many=True)
        return Response(serializer.data)
