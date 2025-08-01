from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from .models import Appointment
from services.models import Service
from datetime import datetime, date

def book_appointment(request, service_id=None):
    services = Service.objects.filter(is_active=True)
    selected_service = None
    
    if service_id:
        selected_service = get_object_or_404(Service, id=service_id, is_active=True)

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email', '')
        service_id = request.POST.get('service')
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        notes = request.POST.get('notes', '')

        try:
            service = Service.objects.get(id=service_id)
            
            appointment = Appointment.objects.create(
                name=name,
                phone=phone,
                email=email,
                service=service,
                appointment_date=appointment_date,
                appointment_time=appointment_time,
                notes=notes
            )
            
            messages.success(request, 'Votre rendez-vous a été enregistré! Nous vous contacterons pour confirmation.')
            return redirect('appointments:success')
            
        except Exception as e:
            messages.error(request, 'Une erreur est survenue. Veuillez réessayer.')

    context = {
        'services': services,
        'selected_service': selected_service,
        'today': date.today().isoformat(),
    }
    return render(request, 'appointments/book.html', context)

def booking_success(request):
    return render(request, 'appointments/success.html')

@staff_member_required
def admin_dashboard(request):
    appointments = Appointment.objects.all()
    
    status_filter = request.GET.get('status')
    if status_filter:
        appointments = appointments.filter(status=status_filter)
    
    # Handle status updates
    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        new_status = request.POST.get('status')
        
        try:
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.status = new_status
            appointment.save()
            messages.success(request, f'Statut du rendez-vous mis à jour: {appointment.get_status_display()}')
        except Appointment.DoesNotExist:
            messages.error(request, 'Rendez-vous introuvable.')
        
        return redirect('appointments:dashboard')

    context = {
        'appointments': appointments,
        'selected_status': status_filter,
        'status_choices': Appointment.STATUS_CHOICES,
    }
    return render(request, 'appointments/dashboard.html', context)