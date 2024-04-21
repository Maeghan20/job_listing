from django.urls import path

from . import views

app_name='jobapp'


urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.jb, name='upload'),
]