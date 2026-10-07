from rest_framework.urls import path
from turf_reservation_v2.views import SignupView,BookingCreateListView


urlpatterns=[

    path('signup/',SignupView.as_view()),
    path('reservations/',BookingCreateListView.as_view())

]