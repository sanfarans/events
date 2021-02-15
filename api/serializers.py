from django.db.models import fields
from rest_framework import serializers
from rest_framework.utils import field_mapping
from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'start_date', 'end_date', 'thumbnail')