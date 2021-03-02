from rest_framework import serializers
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
            return Response(serializer.data)
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
            return Response({'response': 'No reservation with such code in the database'})
        event = ReservationCodeSerializer(reservation).data["event"]
        resp = {'event': event, 'code': code}
        return Response(resp)
    
    def post(self, request):
        code = request.data["code"]
        try:
            reservation = ReservationCode.objects.get(code=code)
        except:
            return Response({'response': 'No reservation with such code in the database'})
        
        event = reservation.event
        length_in_days = int(str(event.end_date - event.start_date).split()[0])
        if length_in_days > 2:
            return Response({'response': "You can't cancel registration for event that lasts longer than two days"})
        today = date.today()
        print(event.start_date, today)
        days_until_event = int(str(event.start_date - today).split()[0])
        print(days_until_event)
        if days_until_event < 0:
            return Response({'response': "Event already started"})
        if days_until_event < 2:
            return Response({'response': "You can't cancel registration for event that's starting in two days or sooner"})
        reservation.delete()
        return Response({'response': 'Successfully cancelled'})
