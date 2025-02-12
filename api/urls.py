from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name = 'posts'),
    path('posts/<uuid:pk>/', views.PostDetailUpdateView.as_view(), name = 'readupdate')
]

