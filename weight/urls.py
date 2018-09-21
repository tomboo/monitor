from django.urls import path
from weight import views


urlpatterns = [
    path('', views.index, name='index'),
    path('weights/', views.weights, name='weights'),
    path('weights/data/', views.weights_data, name='weights_data'),
]
