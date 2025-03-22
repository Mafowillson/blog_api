from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name = 'posts'),
    path('posts/<uuid:pk>/', views.PostDetailUpdateView.as_view(), name = 'readupdate'),
    path('posts/signup/', views.RegisterView.as_view(), name='register'),
    path('posts/create/', views.PostCreateView.as_view(), name='create'),
    path('posts/login/', views.LoginView.as_view(), name='login'),
    path('posts/delete/<uuid:pk>/', views.PostDeleteView.as_view(), name='delete'),
]

