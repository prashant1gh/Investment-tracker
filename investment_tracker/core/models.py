from django.db import models


class Investment(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    initial_amount_invested = models.FloatField()

    def __str__(self):
        return self.name

class Product(models.Model):
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    rate = models.FloatField()
    quantity = models.FloatField()
    selling_date = models.DateField()

    def __str__(self):
       return self.name

class Expense(models.Model):
    date = models.DateField()
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    expense_amount = models.FloatField()

    def __str__(self):
        return self.title
