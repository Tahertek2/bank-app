from django.shortcuts import render
from rest_framework import generics
from bank.models import Operateur
from bank.serializers import OperateurSerializer, AccountSerializer, CardSerializer, CardTypeSerializer, TransactionSerializer, EmployeeSerializer
from bank.models import Account, Operateur, Card, CardType, Transaction, Employee

class OperatorView(generics.ListAPIView):
    queryset = Operateur.objects.all()
    serializer_class = OperateurSerializer

class AccountView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class CardView(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class CardTypeView(generics.ListAPIView):
    queryset = CardType.objects.all()
    serializer_class = CardTypeSerializer

class TransactionView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class EmployeeView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

def operator_list(request):
    operators = Operateur.objects.all()
    serializer = OperateurSerializer(operators, many=True)
    Operateur_list = Operateur.objects.all()
    return render(request, 'bank.html', {'operators': serializer.data})
