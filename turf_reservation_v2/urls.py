from rest_framework.urls import path
from turf_reservation_v2.views import SignupView


urlpatterns=[

    path('signup/',SignupView.as_view()),

]