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
            "message": "Event Created Successfully",
            "id": event.pk,
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


class EventDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event)
            response_data = {
                "event": serializer.data,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except Event.DoesNotExist:
            return Response(
                {"detail": "Event not found"}, status=status.HTTP_404_NOT_FOUND
            )
