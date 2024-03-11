from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category


@api_view(['GET'])
def list_categories(request):
    categories = Category.objects.all()

    if categories:
        result = [{'id': category.id, 'name': category.name} for category in categories]
        return Response({'categories': result}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'No categories found'}, status=status.HTTP_404_NOT_FOUND)
