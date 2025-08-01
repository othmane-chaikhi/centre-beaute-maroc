from django.shortcuts import render, get_object_or_404
from .models import Service, ServiceCategory

def service_list(request):
    categories = ServiceCategory.objects.all()
    services = Service.objects.filter(is_active=True)
    
    category_filter = request.GET.get('category')
    if category_filter:
        services = services.filter(category_id=category_filter)
    
    context = {
        'categories': categories,
        'services': services,
        'selected_category': int(category_filter) if category_filter else None,
    }
    return render(request, 'services/list.html', context)

def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id, is_active=True)
    related_services = Service.objects.filter(
        category=service.category, 
        is_active=True
    ).exclude(id=service_id)[:3]
    
    context = {
        'service': service,
        'related_services': related_services,
    }
    return render(request, 'services/detail.html', context)