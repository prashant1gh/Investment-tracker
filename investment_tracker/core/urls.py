from django.urls import path
from . import views


urlpatterns = [
    path('', views.investment_stat, name='investment_stat'),
    path('investment-details/<int:investment_id>/', views.investment_details, name='investment_details'),
    path('expenses/', views.expenses, name='expenses'),
    path('products/', views.products, name='products'),
    path('add-investment/', views.add_investment, name='add_investment'),
    path('edit-investment/<int:investment_id>', views.edit_investment, name='edit_investment'),
    path('delete-investment/<int:investment_id>', views.delete_investment, name='delete_investment'),
    path('add-product/', views.add_product, name='add_product'),
    path('edit-product/<int:product_id>', views.edit_product, name='edit_product'),
    path('delete-product/<int:product_id>', views.delete_product, name='delete_product'),
    path('add-expense/', views.add_expense, name='add_expense'),
    path('edit-expense/<int:expense_id>', views.edit_expense, name='edit_expense'),
    path('delete-expense/<int:expense_id>', views.delete_expense, name='delete_expense'),
]