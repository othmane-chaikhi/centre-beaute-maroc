from django.db import models

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")
    description = models.TextField(blank=True, verbose_name="Description")
    icon = models.CharField(max_length=50, blank=True, verbose_name="Icône Font Awesome")

    class Meta:
        verbose_name = "Catégorie de Service"
        verbose_name_plural = "Catégories de Services"

    def __str__(self):
        return self.name

class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, verbose_name="Catégorie")
    name = models.CharField(max_length=100, verbose_name="Nom du service")
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Prix (MAD)")
    duration = models.IntegerField(help_text="Durée en minutes", verbose_name="Durée")
    image = models.ImageField(upload_to='services/', blank=True, verbose_name="Image")
    is_featured = models.BooleanField(default=False, verbose_name="Service vedette")
    is_active = models.BooleanField(default=True, verbose_name="Actif")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['category', 'name']

    def __str__(self):
        return f"{self.name} - {self.price} MAD"

    def get_duration_display(self):
        hours = self.duration // 60
        minutes = self.duration % 60
        if hours > 0:
            return f"{hours}h{minutes:02d}"
        return f"{minutes} min"