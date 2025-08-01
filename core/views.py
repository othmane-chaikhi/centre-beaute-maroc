from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Review, ContactInfo
from services.models import Service

def home(request):
    featured_services = Service.objects.filter(is_featured=True)[:3]
    reviews = Review.objects.filter(is_approved=True)[:6]
    
    context = {
        'featured_services': featured_services,
        'reviews': reviews,
    }
    return render(request, 'core/home.html', context)

def contact(request):
    contact_info = ContactInfo.objects.first()
    reviews = Review.objects.filter(is_approved=True)[:10]
    
    context = {
        'contact_info': contact_info,
        'reviews': reviews,
    }
    return render(request, 'core/contact.html', context)

def add_review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        
        Review.objects.create(
            name=name,
            rating=rating,
            comment=comment
        )
        
        messages.success(request, 'Merci pour votre avis! Il sera visible après approbation.')
        return redirect('core:contact')
    
    return redirect('core:contact')