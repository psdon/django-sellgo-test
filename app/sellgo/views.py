import pandas as pd
from django.shortcuts import get_list_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import CsvProduct, Customer
from .serializers import (
    CreateCsvProductSerializer,
    CsvProductSerializer,
    CustomerSerializer,
)
from .services import save_csv_product


class CustomerViewSet(
    viewsets.GenericViewSet, viewsets.mixins.CreateModelMixin
):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CsvProductViewSet(
    viewsets.GenericViewSet,
):
    queryset = CsvProduct.objects.all()
    serializer_class = CreateCsvProductSerializer

    @staticmethod
    def create(request):
        """Create products based on uploaded CSV file.

        Arguments:
            request: Obj

        Returns:
            CsvProduct Fields
        """
        customer_id = request.data["customer_id"]
        csv_file = request.FILES["csv"]

        dataframe = pd.read_csv(csv_file)
        dataframe["customer_id"] = int(customer_id)

        # make columns lower case
        dataframe.columns = map(str.lower, dataframe.columns)

        data = dataframe.to_dict("record")
        save_csv_product(data)
        return Response(data=data, status=status.HTTP_201_CREATED)

    @staticmethod
    def retrieve(_, pk=None):
        """Retrive latest customer products.

        Arguments:
            pk: Customer ID

        Returns:
            {
                "customer_id": CsvProduct.customer.id,
                "customer_name": CsvProduct.customer.name,
                "product_id": CsvProduct.id,
                "product_title": CsvProduct.title,
                "product_price": CsvProduct.price,
                "last_uploaded": CsvProduct.uploaded_date
            }
        """
        queryset = (
            CsvProduct.objects.order_by("-uploaded_date")
            .order_by("title", "-uploaded_date")
            .distinct("title")
        )

        objs = get_list_or_404(queryset, customer__id=pk)

        products = []
        for obj in objs:
            data = {
                "customer_id": obj.customer.id,
                "customer_name": obj.customer.name,
                "product_id": obj.id,
                "product_title": obj.title,
                "product_price": obj.price,
                "last_uploaded": obj.uploaded_date,
            }
            products.append(data)

        serializer = CsvProductSerializer(data=products, many=True)
        serializer.is_valid(True)

        return Response(data=serializer.data)
