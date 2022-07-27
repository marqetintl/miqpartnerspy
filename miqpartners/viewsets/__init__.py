

from rest_framework import viewsets, serializers
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
# from rest_framework.response import Response

from miq.staff.mixins import LoginRequiredMixin
from miq.core.permissions import DjangoModelPermissions

from ..models import Partner
from ..serializers import PartnerSerializer


#
# PRIVATE API
#

class Mixin(LoginRequiredMixin):
    lookup_field = 'slug'
    parser_classes = (JSONParser, )
    permission_classes = (IsAdminUser, DjangoModelPermissions)


class PartnerViewset(Mixin, viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = []

    @action(methods=['patch'], detail=True, url_path=r'extra/')
    def extra(self, *args, ** kwargs):
        obj = self.get_object()
        obj.extra = {**obj.extra, **self.request.data}
        obj.save()
        return self.retrieve(*args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        # params = self.request.query_params

        # q = params.get('q')
        # if q:
        #     qs = qs.find(q)

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
