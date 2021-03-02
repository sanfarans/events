from django.db.models import fields
from rest_framework import serializers
from events.models import Event, ReservationCode, random_string


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'start_date', 'end_date', 'thumbnail')


class ReservationCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationCode
        fields = ('event',)
