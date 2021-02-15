from django.urls import path
from .views import EventListView, RegistrationView, ReservationView

urlpatterns = [
    path('', EventListView.as_view(), name='home'),
    path('register/', RegistrationView.as_view(), name='registration'),
    path('reservation/<str:code>/', ReservationView.as_view(), name='reservation'),
]