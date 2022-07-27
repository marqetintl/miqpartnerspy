

# from django.contrib.sites.shortcuts import get_current_site
from django.utils.translation import gettext_lazy as _


from miq.core.views.generic import TemplateView

from ..models import Partner
from ..serializers import PartnerSerializer


class PartnerOnboardView(TemplateView):
    template_name = 'miqpartners/base.django.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        slug = self.request.session.get('_par')

        data = {}
        if slug and (partner := Partner.objects.filter(slug=slug)):
            data['partner'] = PartnerSerializer(partner.first()).data

        self.update_sharedData(ctx, data)
        return ctx
