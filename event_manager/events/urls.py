from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'), 
    path('add/', views.add_event, name='add_event'),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),
]
