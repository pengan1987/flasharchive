from django.conf.urls import url  

from . import views

urlpatterns = [
    url(r'player',views.retroplayer),
    url(r'', views.retroindex),

]