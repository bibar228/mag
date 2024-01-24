
from django.contrib import admin

# Register your models here.
from trans.models import Bill, Transactions


class BillAdmin(admin.ModelAdmin):
    list_display = ["id", 'user', "balance"]

admin.site.register(Bill, BillAdmin)


class TransactionsAdmin(admin.ModelAdmin):
    list_display = ["id", "bill", 'user', "amount"]

admin.site.register(Transactions, TransactionsAdmin)