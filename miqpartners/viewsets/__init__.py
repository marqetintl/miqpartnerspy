
from collections import OrderedDict
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response

from miq.staff.mixins import LoginRequiredMixin
from miq.core.permissions import DjangoModelPermissions
from miq.core.pagination import MiqPageNumberPagination
from miq.utils import get_ig_username_info, map_ig_graphql_to_user

from ..models import Partner
from ..serializers import PartnerSerializer


#
# PRIVATE API
#

class Pagination(MiqPageNumberPagination):
    page_size = 100


class Mixin(LoginRequiredMixin):
    lookup_field = 'slug'
    parser_classes = (JSONParser, )
    pagination_class = Pagination
    permission_classes = (IsAdminUser, DjangoModelPermissions)


class PartnerViewset(Mixin, viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = []

    def get_queryset(self):
        qs = super().get_queryset()
        params = self.request.query_params

        if params.get('is_newbie') == 'true':
            qs = qs.filter(extra__is_newbie='oui')
        if params.get('wears_lingerie') == 'true':
            qs = qs.filter(extra__wears_lingerie='oui')

        return qs

    def perform_create(self, serializer):
        partner = serializer.save()
        session = self.request.session
        value = session.get('_par')
        slug = f'{partner.slug}'
        if not value:
            session['_par'] = slug
            return

        if value != slug:
            # TODO: ??
            session['_par'] = slug


cache = OrderedDict()


@api_view(['GET'])
@permission_classes([])
def partner_audit_view(request):
    params = request.query_params
    username = params.get('username')
    if not username:
        return Response({'username': 'Required'}, status=400)

    res = cache.get(username)
    if not res:
        print('Getting data')
        res = get_ig_username_info(username)
        if not res:
            return Response({'username': 'Not found'}, status=404)

        if (len(cache.keys()) == 100):
            cache.popitem(last=False)

        cache[username] = res

    if 'graphql' in res.keys():
        res = map_ig_graphql_to_user(res)

    return Response(res)
