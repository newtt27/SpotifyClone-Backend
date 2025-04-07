from django.urls import path
from . import views

#Cấu hình URL cho ứng dụng music
urlpatterns = [
    path('', views.get_music),
]