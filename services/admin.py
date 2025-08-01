from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Service, ServiceCategory

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'icon', 'service_count']
    search_fields = ['name']
    list_per_page = 20
    
    def service_count(self, obj):
        count = obj.service_set.count()
        if count > 0:
            url = reverse('admin:services_service_changelist') + f'?category__id__exact={obj.id}'
            return format_html('<a href="{}">{} service(s)</a>', url, count)
        return '0 service'
    service_count.short_description = 'Nombre de services'

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price_display', 'duration_display', 'is_featured', 'is_active', 'created_at']
    list_filter = ['category', 'is_featured', 'is_active', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['is_featured', 'is_active']
    list_per_page = 20
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Informations Générales', {
            'fields': ('name', 'category', 'description')
        }),
        ('Tarification et Durée', {
            'fields': ('price', 'duration')
        }),
        ('Image et Options', {
            'fields': ('image', 'is_featured', 'is_active')
        }),
    )
    
    def price_display(self, obj):
        return f"{obj.price} MAD"
    price_display.short_description = 'Prix'
    price_display.admin_order_field = 'price'
    
    def duration_display(self, obj):
        return obj.get_duration_display()
    duration_display.short_description = 'Durée'
    duration_display.admin_order_field = 'duration'
    
    actions = ['make_featured', 'remove_featured', 'activate_services', 'deactivate_services']
    
    def make_featured(self, request, queryset):
        updated = queryset.update(is_featured=True)
        self.message_user(request, f'{updated} service(s) marqué(s) comme vedette.')
    make_featured.short_description = "Marquer comme service vedette"
    
    def remove_featured(self, request, queryset):
        updated = queryset.update(is_featured=False)
        self.message_user(request, f'{updated} service(s) retiré(s) des services vedettes.')
    remove_featured.short_description = "Retirer des services vedettes"
    
    def activate_services(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, f'{updated} service(s) activé(s).')
    activate_services.short_description = "Activer les services sélectionnés"
    
    def deactivate_services(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, f'{updated} service(s) désactivé(s).')
    deactivate_services.short_description = "Désactiver les services sélectionnés"