from django.urls import path

from .views import stop_car_views

urlpatterns = [
    path('', stop_car_views.index, name='index'),
    path('stop_car/query', stop_car_views.query),
    path('stop_car/run', stop_car_views.run),
]
