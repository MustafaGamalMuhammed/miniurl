from django.urls import path
from url_shortener import views


urlpatterns = [
    path('', views.index, name="index"),
    path('shorten_url/', views.shorten_url, name="shorten_url"),
    path('<str:key>/', views.get_url, name="get_url"),
]