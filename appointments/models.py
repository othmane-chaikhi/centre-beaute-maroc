from django.db import models
from services.models import Service

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('confirmed', 'Confirmé'),
        ('cancelled', 'Annulé'),
        ('completed', 'Terminé'),
    ]

    name = models.CharField(max_length=100, verbose_name="Nom complet")
    phone = models.CharField(max_length=20, verbose_name="Téléphone")
    email = models.EmailField(blank=True, verbose_name="Email")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Service")
    appointment_date = models.DateField(verbose_name="Date du rendez-vous")
    appointment_time = models.TimeField(verbose_name="Heure du rendez-vous")
    notes = models.TextField(blank=True, verbose_name="Notes supplémentaires")
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='pending',
        verbose_name="Statut"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Rendez-vous"
        verbose_name_plural = "Rendez-vous"
        ordering = ['-appointment_date', '-appointment_time']

    def __str__(self):
        return f"{self.name} - {self.service.name} - {self.appointment_date}"

    @property
    def is_pending(self):
        return self.status == 'pending'