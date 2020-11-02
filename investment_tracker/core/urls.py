from django.urls import path
from . import views


urlpatterns = [
    path('', views.investment_stat, name='investment_stat'),
    path('investment-details/<int:investment_id>/', views.investment_details, name='investment_details'),
    path('expenses/', views.expenses, name='expenses'),
    path('products/', views.products, name='products'),
]