from django.conf.urls import url
from ydownloader import views

urlpatterns = [
	url(r'^https://youtube-to-mp3-convert.herokuapp.com/$',views.greetings),
    url(r'^home/download/$',views.download),
    url(r'^home/downloading/$',views.downloading),
    
 ]
