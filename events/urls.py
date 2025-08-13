from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name= 'index.html'),
    path('event/<int:event>/', views.event, name="event.html")


]