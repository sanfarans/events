from django.urls import path
from .views import EventAPIView, RegisterAPIView, ManageReservationAPIView

urlpatterns = [
    path('', EventAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('manage/', ManageReservationAPIView.as_view()),
]