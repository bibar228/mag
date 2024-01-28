from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from trans.models import Bill
from trans.serializers import TransactionsSerializer, BillSerializer


class TransactionsView(APIView):
    serializer_class = TransactionsSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # создание номера заказа с характеристиками
        serializer = TransactionsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        sv = serializer.save()

        if sv[0] == "bill not found":
            return Response({"resultCode": [1], "message": ["BILL NOT FOUND"]})

        if sv[0] == "user not found":
            return Response({"resultCode": [1], "message": ["USER NOT FOUND"]})

        if sv[0] == "USER DONT HAVE THIS BILL, ERROR":
            return Response({"resultCode": [1], "message": ["USER DONT HAVE THIS BILL, ERROR"]})

        count = sv[0].amount + Bill.objects.filter(id=sv[1])[0].balance
        Bill.objects.filter(id=sv[1]).update(balance=count)
        return Response({"resultCode": [0], "message": ["Transaction was successful"], "user": {str(sv[0].user)}})


class BillCreateView(APIView):
    serializer_class = BillSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # создание номера заказа с характеристиками
        serializer = BillSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        sv = serializer.save()
        if sv == 1:
            return Response({"resultCode": [1], "message": ["ERROR CREATE BILL"]})
        else:
            return Response({"resultCode": [0], "message": ["Bill was successful create"]})