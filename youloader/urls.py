from django.urls import path
from youloader import views


urlpatterns = [
	path('',views.index),
	path('video/<str:id>/',views.video_details, name='video_details'),
	path('download/<str:id>/',views.download_audio, name='download_audio')
    # path(r'^home/download/$',views.download),
    # path(r'home/downloading/$',views.downloading),
]