from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import DataSheet
from .serializers import DataSheetSerializer
from ..product.models import Product


@api_view(['GET'])
def list_data_sheet_by_product(request, product_id):
    if product_id:
        product = get_object_or_404(Product, id=product_id)
        datasheets = DataSheet.objects.filter(product=product)
        serializer = DataSheetSerializer(datasheets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Product ID is required'}, status=status.HTTP_400_BAD_REQUEST)
