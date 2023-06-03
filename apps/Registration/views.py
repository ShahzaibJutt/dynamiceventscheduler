from rest_framework import status, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.Event.models import Event
from apps.Registration.models import Registration
from apps.Registration.serializers import RegistrationSerializer


class RegistrationCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        # Get the event ID from the request data
        event_id = request.data.get('event_id')

        # Retrieve the Event object based on the event_id
        event = get_object_or_404(Event, id=event_id)

        # Save the Registration with the user and event
        # registration = serializer.save(commit=False, user=request.user, event=event)
        serializer.is_valid(raise_exception=True)
        registration = serializer.save(user=request.user, event=event)

        response_data = {
            "message": "Registration Created Successfully",
            "registration_id": registration.id
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


class UserRegistrationListAPIView(generics.ListAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Registration.objects.filter(user=user).select_related('event')
