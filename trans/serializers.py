from rest_framework import serializers

from trans.models import Transactions, Bill

from cryptohash import sha1
from users.models import User


class TransactionsSerializer(serializers.Serializer):
    bill = serializers.IntegerField()
    user = serializers.IntegerField()
    amount = serializers.IntegerField()

    class Meta:
        model = Transactions
        fields = ["bill", "user", "amount"]

    def save(self, *args, **kwargs):
        try:
            bill = Bill.objects.filter(id=self.validated_data["bill"]).get()
        except:
            return "bill not found", 1

        try:
            user = User.objects.filter(id=self.validated_data["user"]).get()
        except:
            return "user not found", 1

        if str(bill) != str(user):
            return "USER DONT HAVE THIS BILL, ERROR", 1

        order = Transactions(
            signature=sha1(f'{self.validated_data["user"]}:{self.validated_data["bill"]}:{self.validated_data["amount"]}'),
            bill=bill,
            user=user,
            amount=self.validated_data["amount"]
        )
        bill = self.validated_data["bill"]
        order.save()
        return order, bill

class BillSerializer(serializers.Serializer):
    login = serializers.CharField()

    class Meta:
        model = Transactions
        fields = ["balance"]

    def save(self, *args, **kwargs):
        try:
            user = User.objects.filter(login=self.validated_data["login"]).get()
            print(user)
            order = Bill(
                user=user
            )

            order.save()
            return order
        except Exception as e:
            return 1
