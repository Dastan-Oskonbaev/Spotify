from django.urls import path
from .views import hello, about, album
from . import views

urlpatterns = [
    path('', hello, name='hello'),
    path('about', about, name='about'),
    path('album', album, name='album'),
    path('authors_list', views.authors_list, name='authors_list'),
    path('authors_list_2', views.AuthorsListView.as_view(), name='authors_list_2'),
]