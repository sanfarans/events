from django.urls import path
from .views import EventListView, ReservationView, ReservationManageView

urlpatterns = [
    path('', EventListView.as_view(), name='home'),
    path('reservation/new/', ReservationView.as_view(), name='reservation_new'),
    path('manage/', ReservationManageView.as_view(), name='reservation_manage'),
]