from django.shortcuts import render
from .models import Income,Expense

def main(request):
    return render(request, 'main.html')

def management(request):
    income = Income.objects.order_by('-time')
    return render(request, 'table.html',{'income':income})

