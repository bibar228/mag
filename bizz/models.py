from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title