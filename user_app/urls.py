from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'user_app'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='user_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('user_create/', views.UserCreate.as_view(), name='user_create'),
    path('user_detail/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('user_update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
]
