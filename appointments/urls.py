from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('book/', views.book_appointment, name='book'),
    path('book/<int:service_id>/', views.book_appointment, name='book_service'),
    path('success/', views.booking_success, name='success'),
    path('dashboard/', views.admin_dashboard, name='dashboard'),
]