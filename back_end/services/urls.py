from django.urls import path

from . import views

urlpatterns = [
    path('request', views.RequestCreateView.as_view()),
    path('sector', views.SectorListView.as_view()),
]