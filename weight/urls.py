from django.urls import path
from weight import views


urlpatterns = [
    path('', views.index, name='index'),
]
