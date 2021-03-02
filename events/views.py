from events.forms import ReservationForm
from django.views import View
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from .models import Event, ReservationCode
from datetime import date


class EventListView(View):
    model = Event
    template_name = 'event_list.html'
    event_list = Event.objects.order_by('start_date')
    
    def get(self, request):
        context = {'event_list': self.event_list}
        return render(request, self.template_name, context)


class ReservationView(View):
    template_name = 'registration_new.html'
    model = ReservationCode

    def get(self, request):
        form = ReservationForm()
        context = {'form': form }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = ReservationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, self.template_name, context)


class ReservationManageView(View):
    template_name = 'reservation.html'

    def get(self, request):
        code = request.GET['code']
        reservation = get_object_or_404(ReservationCode, code=code)
        context = {'reservation': reservation}
        return render(request, self.template_name, context)
    
    def post(self, request):
        code = request.POST['code']
        reservation = get_object_or_404(ReservationCode, code=code)
        event = reservation.event
        length_in_days = int(str(event.end_date - event.start_date).split()[0])
        if length_in_days > 2:
            return HttpResponse("<h1>You can't cancel registration for event that lasts longer than two days</h1>")
        today = date.today()
        print(event.start_date, today)
        days_until_event = int(str(event.start_date - today).split()[0])
        print(days_until_event)
        if days_until_event < 0:
            return HttpResponse("<h1>Event already started</h1>")
        if days_until_event < 2:
            return HttpResponse("<h1>You can't cancel registration for event that's starting in two days or sooner</h1>")
        reservation.delete()
        return redirect('home')
