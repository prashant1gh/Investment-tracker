from django.shortcuts import render, get_object_or_404, redirect
from .forms import InvestmentForm, ProductForm, ExpenseForm
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


def add_investment(request):
    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print('form invalid')
        
    else:
        form = InvestmentForm()
    
    return render(request, 'add_investment.html', {'form': form})

def edit_investment(request, investment_id):
    investment = get_object_or_404(Investment, pk=investment_id)
    form = InvestmentForm(request.POST or None, instance=investment)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'add_investment.html', {'form': form})


def delete_investment(request, investment_id):
    investment = get_object_or_404(Investment, pk=investment_id)
    investment.delete()
    return redirect('/')


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products/')
        else:
            print('form invalid')
        
    else:
        form = ProductForm()
    
    return render(request, 'add_product.html', {'form': form})

def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('/products/')
    return render(request, 'add_product.html', {'form': form})


def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect('/products/')


def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/expenses/')
        else:
            print('form invalid')
        
    else:
        form = ExpenseForm()
    
    return render(request, 'add_expense.html', {'form': form})

def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)
    form = ExpenseForm(request.POST or None, instance=expense)
    if form.is_valid():
        form.save()
        return redirect('/expenses/')
    return render(request, 'add_expense.html', {'form': form})


def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)
    expense.delete()
    return redirect('/expenses/')
