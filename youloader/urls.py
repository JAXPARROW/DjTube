from django.urls import path
from youloader import views


urlpatterns = [
	path('',views.index),
    # path(r'^home/download/$',views.download),
    # path(r'home/downloading/$',views.downloading),
]