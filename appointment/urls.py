from django.urls import path
from appointment.views import receprion


urlpatterns = [
    path('', receprion, name='index'),
]
