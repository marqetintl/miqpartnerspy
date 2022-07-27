"""
# PUBLIC API
"""

# from rest_framework import viewsets, serializers
# from rest_framework.parsers import JSONParser
# from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# from ..models import Partner
from .serializers import PartnerSerializer


@api_view(['POST'])
@permission_classes([])
def create_partner_view(request):

    data = request.data
    extra = {
        'age': data.pop('age', None),
        'size': data.pop('size', None),
        'interests': data.pop('interests', []),
        'pay': data.pop('pay', None),
        'wears_lingerie': data.pop('wears_lingerie', False),
        'is_newbie': data.pop('is_newbie', True),
    }
    ser = PartnerSerializer(data=data)
    ser.is_valid(raise_exception=True)
    ser.save(extra=extra)

    return Response(ser.data, status=201)
