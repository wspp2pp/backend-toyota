from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer
from ..category.models import Category


@api_view(['GET'])
def list_product_by_category(request, category_id):
    if category_id.isdigit():
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Category ID is required'}, status=status.HTTP_400_BAD_REQUEST)
