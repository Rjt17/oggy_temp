from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="home-index"),
    path('restaurant/', views.restaurant, name='home-rest')
]
