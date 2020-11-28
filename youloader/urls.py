from django.urls import path
from youloader import views


urlpatterns = [
	path('',views.index),
	path('download_audio',views.download_audio, name='download_audio')
    # path(r'^home/download/$',views.download),
    # path(r'home/downloading/$',views.downloading),
]