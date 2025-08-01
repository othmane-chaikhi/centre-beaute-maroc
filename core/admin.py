from django.contrib import admin
from django.utils.html import format_html
from .models import Review, ContactInfo

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating_display', 'is_approved', 'created_at', 'comment_preview']
    list_filter = ['rating', 'is_approved', 'created_at']
    search_fields = ['name', 'comment']
    list_editable = ['is_approved']
    list_per_page = 20
    date_hierarchy = 'created_at'
    actions = ['approve_reviews']
    
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Informations Client', {
            'fields': ('name', 'rating')
        }),
        ('Avis', {
            'fields': ('comment', 'is_approved')
        }),
        ('Métadonnées', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def rating_display(self, obj):
        stars = '★' * obj.rating + '☆' * (5 - obj.rating)
        return format_html('<span style="color: #ffc107;">{}</span> ({})', stars, obj.rating)
    rating_display.short_description = 'Note'
    rating_display.admin_order_field = 'rating'
    
    def comment_preview(self, obj):
        if len(obj.comment) > 50:
            return obj.comment[:50] + '...'
        return obj.comment
    comment_preview.short_description = 'Aperçu du commentaire'

    def approve_reviews(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, f"{queryset.count()} avis approuvés.")
    approve_reviews.short_description = "Approuver les avis sélectionnés"

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['phone', 'address_preview', 'has_map']
    
    fieldsets = (
        ('Coordonnées', {
            'fields': ('phone', 'address')
        }),
        ('Horaires', {
            'fields': ('hours',)
        }),
        ('Carte', {
            'fields': ('map_embed',),
            'description': 'Coller ici le code d\'intégration Google Maps (iframe)'
        }),
    )
    
    def address_preview(self, obj):
        if len(obj.address) > 50:
            return obj.address[:50] + '...'
        return obj.address
    address_preview.short_description = 'Adresse'
    
    def has_map(self, obj):
        return bool(obj.map_embed)
    has_map.boolean = True
    has_map.short_description = 'Carte intégrée'

    def has_add_permission(self, request):
        return not ContactInfo.objects.exists()