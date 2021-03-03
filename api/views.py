from rest_framework import serializers
from rest_framework import status
from events.models import Event, ReservationCode, random_string
from .serializers import EventSerializer, ReservationCodeSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from datetime import date

class EventAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        serializer = EventSerializer(Event.objects.all(), many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class RegisterAPIView(APIView):

    def post(self, request):
        serializer = ReservationCodeSerializer(data=request.data)
        if serializer.is_valid():
            event = serializer.data["event"]
            code = random_string()
            obj = ReservationCode(event=Event.objects.get(pk=event), code=code)
            obj.save()
            resp = {'event': event, 'code': code}
            return Response(resp)
        return Response(serializer.errors)


class ManageReservationAPIView(APIView):

    def get(self, request):
        code = request.query_params.get('code')
        try:
            reservation = ReservationCode.objects.get(code=code)
        except:
            message = 'No reservation with such code in the database'
            return Response({'response': message}, status=status.HTTP_404_NOT_FOUND)
        event = ReservationCodeSerializer(reservation).data["event"]
        resp = {'event': event, 'code': code}
        return Response(resp)
    
    def delete(self, request):
        code = request.data["code"]
        try:
            reservation = ReservationCode.objects.get(code=code)
        except:
            message = 'No reservation with such code in the database'
            return Response({'response': message}, status=status.HTTP_404_NOT_FOUND)
        
        event = reservation.event
        length_in_days = int(str(event.end_date - event.start_date).split()[0])
        if length_in_days > 2:
            message = "You can't cancel registration for event that lasts longer than two days"
            return Response({'response': message}, status=status.HTTP_409_CONFLICT)
        today = date.today()
        days_until_event = int(str(event.start_date - today).split()[0])
        if days_until_event < 0:
            message = "Event already started"
            return Response({'response': message}, status=status.HTTP_409_CONFLICT)
        if days_until_event < 2:
            message = "You can't cancel registration for event that's starting in two days or sooner"
            return Response({'response': message}, status=status.status.HTTP_409_CONFLICT)
        reservation.delete()
        return Response({'response': 'Successfully cancelled'}, status=status.HTTP_200_OK)
