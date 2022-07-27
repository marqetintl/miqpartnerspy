
from rest_framework import serializers

from ..models import Partner


class PartnerSerializer(serializers.ModelSerializer):
    class Meta():
        model = Partner
        read_only_fields = ('slug', 'user', 'extra')
        fields = (
            'first_name', 'last_name', 'phone', 'email',
            'tt', 'ig',
            * read_only_fields
        )
