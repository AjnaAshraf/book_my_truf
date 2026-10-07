from rest_framework.urls import path
from turf_reservation_v2.views import SignupView,BookingCreateListView,BookingRetrieveUpdateDeleteView


urlpatterns=[

    path('signup/',SignupView.as_view()),
    path('reservations/',BookingCreateListView.as_view()),
    path('reservations/<int:pk>/',BookingRetrieveUpdateDeleteView.as_view())

]