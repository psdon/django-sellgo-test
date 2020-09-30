from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=254, unique=True)
    created_date = models.DateTimeField(
        auto_now_add=True, editable=False, null=False
    )

    def __str__(self):
        return f"{self.name} | {self.email}"


class CsvProduct(models.Model):
    title = models.CharField(max_length=500, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    uploaded_date = models.DateTimeField(
        auto_now_add=True, editable=False, null=False
    )

    def __str__(self):
        return f"{self.title} | {self.price}"
