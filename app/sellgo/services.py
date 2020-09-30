from .models import CsvProduct, Customer


def save_csv_product(data):

    for product in data:
        customer_obj = Customer.objects.get(pk=product["customer_id"])
        CsvProduct.objects.create(
            title=product["title"],
            price=product["price"],
            customer=customer_obj,
        )
