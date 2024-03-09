from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Info


@api_view(['GET'])
def list_info(request):
    info_objects = Info.objects.all()

    if info_objects:
        info_data = [{'name': info.name, 'url': info.url, 'section': info.section} for info in info_objects]
        return Response({'info': info_data}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'No info found'}, status=status.HTTP_404_NOT_FOUND)
