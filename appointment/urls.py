from django.urls import path, re_path
from django.conf.urls import url
from appointment.views import index, make_record, add_record


urlpatterns = [
    url(r'^doc/', make_record, name='make_record'),
    url(r'^add-record', add_record, name='add_record'),
    path('', index, name='index'),
]
