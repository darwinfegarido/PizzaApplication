
from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('management/', views.ManagementView.as_view(), name='management')
]
