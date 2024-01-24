from django.db import models

from users.models import User


# Create your models here.
class Bill(models.Model):

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Cчета'

    def __str__(self):
        return str(self.user)

class Transactions(models.Model):
    signature = models.CharField(max_length=50)
    bill = models.ForeignKey(Bill, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    amount = models.IntegerField()

    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Транзакции'

