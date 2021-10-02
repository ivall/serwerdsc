from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='Index'),
    path('<name>', views.ServerView.as_view(), name='server-view'),
    path('serwery/', views.ServerListView.as_view(), name='server-list'),
]
