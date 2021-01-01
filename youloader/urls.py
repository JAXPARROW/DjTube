from django.urls import path
from youloader import views


urlpatterns = [
    path('',views.index),
    path('video/<str:id>/',views.video_details, name='video_details'),
    path('get_audio/<str:id>/',views.download_audio, name='download_audio'),
    path('get_video/<str:id>/',views.download_video, name='download_video'),
    # path(r'^home/download/$',views.download),
    # path(r'home/downloading/$',views.downloading),
]