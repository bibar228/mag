from django.db import models

from users.models import User


# Create your models here.
class Accs(models.Model):
    identify = models.CharField(max_length=30)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    balance = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Cчета'

    def __str__(self):
        return self.identify

class Transactions(models.Model):
    count = models.DecimalField(max_digits=15, decimal_places=2)
    accs_id = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Транзакции'

    def __str__(self):
        return self.count