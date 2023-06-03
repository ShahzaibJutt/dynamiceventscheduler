from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.Event.models import Event
from apps.Event.serializers import EventSerializer


class EventCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        event = serializer.save(creater=self.request.user)
        response_data = {
            "message": "Event Created Successfully"
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


class EventListView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def list(self, request, **kwargs):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)
