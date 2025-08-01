from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name="Note")
    comment = models.TextField(verbose_name="Commentaire")
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False, verbose_name="Approuvé")

    class Meta:
        verbose_name = "Avis Client"
        verbose_name_plural = "Avis Clients"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.rating}/5"

class ContactInfo(models.Model):
    phone = models.CharField(max_length=20, verbose_name="Téléphone")
    address = models.TextField(verbose_name="Adresse")
    hours = models.TextField(verbose_name="Heures d'ouverture")
    map_embed = models.TextField(blank=True, verbose_name="Code embed Google Maps")

    class Meta:
        verbose_name = "Informations de Contact"
        verbose_name_plural = "Informations de Contact"

    def __str__(self):
        return "Informations de Contact"