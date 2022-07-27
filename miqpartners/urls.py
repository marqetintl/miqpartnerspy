from django.conf import settings
from django.urls import path, include

from rest_framework import routers

from . import api
from . import views
from . import viewsets


app_name = 'miqpartners'


staff = routers.DefaultRouter()
staff.register(r'partners', viewsets.PartnerViewset)


urlpatterns = [
    path(
        'jobs/ambassadors/', views.PartnerOnboardView.as_view(),
        name='partner_onboard_view'),

    #

    path('api/partners/', api.create_partner_view, name='api_partner_onboard'),
]

urlpatterns += [
    path(f'{settings.API_PATH}/', include(staff.urls)),
]
