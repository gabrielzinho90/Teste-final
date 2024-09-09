from django.db import models

class Consumer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    consumption = models.FloatField()  # Consumo médio
    tariff_type = models.CharField(max_length=20, choices=[('Residencial', 'Residencial'), ('Comercial', 'Comercial'), ('Industrial', 'Industrial')])

    def _str_(self):
        return self.name
