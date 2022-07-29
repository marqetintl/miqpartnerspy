"""
# PUBLIC API
"""

import requests

from rest_framework import serializers
# from rest_framework import viewsets, serializers
# from rest_framework.parsers import JSONParser
# from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# from ..models import Partner
from .serializers import PartnerSerializer

from miq.utils import check_ig_username


@api_view(['POST'])
@permission_classes([])
def create_partner_view(request):
    data = request.data
    if check_ig_username(data.get('ig')) is False:
        raise serializers.ValidationError({'ig': "Ce nom d'utilisateur n'existe pas"})

    pdata = {
        'first_name': data.pop('first_name', None),
        'last_name': data.pop('last_name', None),
        'phone': data.pop('phone', None),
        'email': data.pop('email', None),
        'ig': data.pop('ig', None),
        'tt': data.pop('tt', None),
    }

    ser = PartnerSerializer(data=pdata)
    ser.is_valid(raise_exception=True)
    ser.save(extra=data)
    return Response(ser.data, status=201)

    # extra = {
    #     'age': data.pop('age', None),
    #     'size': data.pop('size', None),
    #     'interests': data.pop('interests', []),
    #     'pay': data.pop('pay', None),
    #     'wears_lingerie': data.pop('wears_lingerie', 'non'),
    #     'is_newbie': data.pop('is_newbie', 'oui'),
    #     'is_sn_active': data.pop('is_sn_active', 'non'),
    # }
