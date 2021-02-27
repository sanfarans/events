from django.db import reset_queries
from events.forms import ReservationForm
from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from .models import Event, ReservationCode


class EventListView(View):
    model = Event
    template_name = 'event_list.html'

    def get(self, request):
        context = {'event_list': Event.objects.all()}
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
        reservation.delete()
        return redirect('home')
