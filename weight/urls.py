from django.urls import path
from weight import views


urlpatterns = [
    path('', views.index, name='index'),
    path('weights/', views.weights, name='weights'),

    path('json-example/', views.json_example, name='json_example'),
    path('json-example/data/', views.chart_data, name='chart_data'),
]
