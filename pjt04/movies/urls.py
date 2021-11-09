from django.urls import path
from . import views

# /movies/ +
app_name = 'movies'
urlpatterns = [
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]