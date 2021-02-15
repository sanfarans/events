from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Event, ReservationCode


class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'


class RegistrationView(CreateView):
    model = ReservationCode
    fields = ['code', 'event', 'reserved']
    template_name = 'registration_new.html'


class ReservationView(UpdateView):
    model = ReservationCode
    fields = ['reserved']
    template_name = 'reservation.html'