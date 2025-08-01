from django.contrib import admin
from django.utils.html import format_html
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'service',
        'appointment_datetime',
        'status',  # Ajouté ici pour autoriser l'édition
        'status_display',
        'phone',
        'created_at'
    ]
    list_filter = ['status', 'service', 'appointment_date', 'created_at']
    search_fields = ['name', 'phone', 'email']
    list_editable = ['status']  # Maintenant valide
    date_hierarchy = 'appointment_date'
    list_per_page = 20

    fieldsets = (
        ('Informations Client', {
            'fields': ('name', 'phone', 'email')
        }),
        ('Détails du Rendez-vous', {
            'fields': ('service', 'appointment_date', 'appointment_time')
        }),
        ('Notes et Statut', {
            'fields': ('notes', 'status')
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ['created_at', 'updated_at']

    actions = ['mark_confirmed', 'mark_cancelled']

    def appointment_datetime(self, obj):
        return f"{obj.appointment_date.strftime('%d/%m/%Y')} à {obj.appointment_time.strftime('%H:%M')}"
    appointment_datetime.short_description = 'Date et Heure'
    appointment_datetime.admin_order_field = 'appointment_date'

    def status_display(self, obj):
        colors = {
            'pending': '#ffc107',
            'confirmed': '#28a745',
            'cancelled': '#dc3545',
            'completed': '#6c757d'
        }
        color = colors.get(obj.status, '#6c757d')
        return format_html(
            '<span style="color: {}; font-weight: bold;">●</span> {}',
            color,
            obj.get_status_display()
        )
    status_display.short_description = 'Statut'
    status_display.admin_order_field = 'status'

    def mark_confirmed(self, request, queryset):
        queryset.update(status='confirmed')
        self.message_user(request, f"{queryset.count()} rendez-vous confirmés.")
    mark_confirmed.short_description = "Marquer comme confirmé"

    def mark_cancelled(self, request, queryset):
        queryset.update(status='cancelled')
        self.message_user(request, f"{queryset.count()} rendez-vous annulés.")
    mark_cancelled.short_description = "Marquer comme annulé"
