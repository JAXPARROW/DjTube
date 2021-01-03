from django.urls import path, re_path
from youloader import views


urlpatterns = [
    path('',views.index),
    re_path('^watch', views.from_youtube, name='from_youtube'),
    path('video/<str:id>/', views.video_details, name='video_details'),
    path('get_audio/<str:id>/', views.download_audio, name='download_audio'),
    path('get_video/<str:id>/',  views.download_video, name='download_video'),

]
