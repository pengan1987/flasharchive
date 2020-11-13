from django.conf.urls import url  

from . import views

urlpatterns = [
    url(r'^list', views.index),
    url(r'', views.index),

]