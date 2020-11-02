from django.shortcuts import render, get_object_or_404

from .models import Investment, Expense, Product

def investment_stat(request):
    investments = Investment.objects.all()
    return render(request, 'investments.html', {'investments': investments})


def investment_details(request, investment_id):
    investment = get_object_or_404(Investment, pk=investment_id)
    return render(request, 'investment-details.html', {'investment': investment})

def expenses(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses.html', {"expenses":expenses})

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {"products":products})