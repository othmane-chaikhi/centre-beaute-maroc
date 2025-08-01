#!/usr/bin/env python
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beauty_center.settings')
django.setup()

from services.models import ServiceCategory, Service
from core.models import ContactInfo, Review
from appointments.models import Appointment
from datetime import date, time

def load_sample_data():
    print("Loading sample data...")
    
    # Create service categories
    coiffure_cat = ServiceCategory.objects.create(
        name="Coiffure",
        description="Services de coiffure professionnels",
        icon="fas fa-cut"
    )
    
    laser_cat = ServiceCategory.objects.create(
        name="Épilation Laser",
        description="Traitements laser pour épilation",
        icon="fas fa-magic"
    )
    
    visage_cat = ServiceCategory.objects.create(
        name="Soins du Visage",
        description="Traitements et soins du visage",
        icon="fas fa-face-smile"
    )
    
    ongles_cat = ServiceCategory.objects.create(
        name="Ongles",
        description="Manucure et pédicure",
        icon="fas fa-hand-sparkles"
    )
    
    # Create services
    services_data = [
        # Coiffure
        {
            'category': coiffure_cat,
            'name': 'Coupe + Brushing',
            'description': 'Coupe personnalisée selon votre style avec brushing professionnel pour une finition parfaite.',
            'price': 150,
            'duration': 90,
            'is_featured': True
        },
        {
            'category': coiffure_cat,
            'name': 'Couleur + Brushing',
            'description': 'Coloration complète avec des produits de qualité supérieure et brushing.',
            'price': 250,
            'duration': 180,
            'is_featured': True
        },
        {
            'category': coiffure_cat,
            'name': 'Mèches + Brushing',
            'description': 'Techniques de mèches modernes pour illuminer votre chevelure.',
            'price': 200,
            'duration': 150
        },
        {
            'category': coiffure_cat,
            'name': 'Traitement Capillaire',
            'description': 'Soins intensifs pour cheveux abîmés avec masques nutritifs.',
            'price': 100,
            'duration': 60
        },
        
        # Laser
        {
            'category': laser_cat,
            'name': 'Épilation Laser Visage',
            'description': 'Épilation définitive du visage avec technologie laser dernière génération.',
            'price': 200,
            'duration': 30,
            'is_featured': True
        },
        {
            'category': laser_cat,
            'name': 'Épilation Laser Jambes Complètes',
            'description': 'Épilation laser pour jambes complètes, résultats durables.',
            'price': 500,
            'duration': 90
        },
        {
            'category': laser_cat,
            'name': 'Épilation Laser Aisselles',
            'description': 'Traitement laser rapide et efficace pour les aisselles.',
            'price': 150,
            'duration': 20
        },
        {
            'category': laser_cat,
            'name': 'Épilation Laser Maillot',
            'description': 'Épilation laser zone maillot avec discrétion et professionnalisme.',
            'price': 300,
            'duration': 45
        },
        
        # Soins du visage
        {
            'category': visage_cat,
            'name': 'Soin Anti-âge',
            'description': 'Traitement anti-âge complet avec produits premium pour retrouver une peau jeune.',
            'price': 300,
            'duration': 75
        },
        {
            'category': visage_cat,
            'name': 'Nettoyage de Peau',
            'description': 'Nettoyage profond pour purifier et rafraîchir votre peau.',
            'price': 180,
            'duration': 60
        },
        {
            'category': visage_cat,
            'name': 'Hydratation Intense',
            'description': 'Soin hydratant en profondeur pour tous types de peau.',
            'price': 220,
            'duration': 60
        },
        
        # Ongles
        {
            'category': ongles_cat,
            'name': 'Manucure Classique',
            'description': 'Manucure complète avec vernis de votre choix.',
            'price': 80,
            'duration': 45
        },
        {
            'category': ongles_cat,
            'name': 'Manucure Gel',
            'description': 'Manucure avec vernis gel longue tenue.',
            'price': 120,
            'duration': 60
        },
        {
            'category': ongles_cat,
            'name': 'Pédicure Spa',
            'description': 'Pédicure relaxante avec bain de pieds et massage.',
            'price': 150,
            'duration': 75
        }
    ]
    
    for service_data in services_data:
        Service.objects.create(**service_data)
    
    # Create contact info
    ContactInfo.objects.create(
        phone="+212 522-123-456",
        address="123 Rue Mohammed V, Casablanca 20000, Maroc",
        hours="Lundi - Vendredi: 9h00 - 19h00\nSamedi: 9h00 - 18h00\nDimanche: Fermé"
    )
    
    # Create sample reviews
    reviews_data = [
        {
            'name': 'Aicha Benjelloun',
            'rating': 5,
            'comment': 'Excellent service ! L\'équipe est très professionnelle et le résultat de ma coloration est parfait. Je recommande vivement !',
            'is_approved': True
        },
        {
            'name': 'Fatima El Alami',
            'rating': 5,
            'comment': 'Très satisfaite de mon épilation laser. Le traitement est efficace et les résultats sont visibles rapidement.',
            'is_approved': True
        },
        {
            'name': 'Khadija Maraoui',
            'rating': 4,
            'comment': 'Salon magnifique et personnel accueillant. Les soins du visage sont de qualité exceptionnelle.',
            'is_approved': True
        },
        {
            'name': 'Salma Bennani',
            'rating': 5,
            'comment': 'Parfait ! Ma manucure gel a tenu 3 semaines sans s\'écailler. Service impeccable.',
            'is_approved': True
        },
        {
            'name': 'Zineb Cherkaoui',
            'rating': 5,
            'comment': 'Centre de beauté moderne avec des équipements de pointe. L\'expérience est toujours agréable.',
            'is_approved': True
        },
        {
            'name': 'Hanane Tazi',
            'rating': 4,
            'comment': 'Très bon accueil et prestations de qualité. Les prix sont raisonnables pour la qualité offerte.',
            'is_approved': True
        }
    ]
    
    for review_data in reviews_data:
        Review.objects.create(**review_data)
    
    print("Sample data loaded successfully!")
    print("\nAdmin access:")
    print("Username: admin")
    print("Password: admin123")
    print("URL: http://localhost:8000/admin/")
    print("\nDashboard: http://localhost:8000/appointments/dashboard/")

if __name__ == '__main__':
    load_sample_data()