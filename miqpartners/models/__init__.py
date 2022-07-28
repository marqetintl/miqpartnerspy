import logging

from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _

from miq.core.models import BaseModelMixin

# from .managers import CustomerManager

logger = logging.getLogger(__name__)
User = get_user_model()


def jsondef():
    return dict({
        'age': None,
        'size': None,

        # store categories choice field
        'interests': [],
        'pay': '',
        # 'compensation': None

        'wears_lingerie': 'non',
        'is_newbie': 'oui',

        # active on social media
        'is_sn_active': 'non',
        # activity frequency
        'active_fq': ''

    })


class PartnerUser(User):
    class Meta:
        proxy = True


class Partner(BaseModelMixin):
    user = models.OneToOneField(
        PartnerUser, related_name='partner',
        null=True, blank=True,
        on_delete=models.PROTECT
    )

    first_name = models.CharField(
        _('First name'), max_length=100,
        # blank=True, null=True,
        validators=[
            MinLengthValidator(2, message=_('Enter your first name.'))
        ])
    last_name = models.CharField(
        _('Last name'), max_length=100,
        # blank=True, null=True,
        validators=[MinLengthValidator(2, message=_('Enter your last name.'))])

    phone = models.CharField(
        _("Phone Number"), max_length=50, unique=True,
        validators=[
            MinLengthValidator(
                4, message=_("Veuillez entrer votre numéro de téléphone.")
            )
        ]
    )

    email = models.EmailField(unique=True, null=True, blank=True)

    # social

    tt = models.CharField(_('Tiktok'), max_length=100, blank=True, null=True)
    ig = models.CharField(_('Instagram'), max_length=100, blank=True, null=True)

    extra = models.JSONField(_("Additional Information"), default=jsondef)

    def save(self, *args, **kwargs):
        if self.email == '':
            self.email = None

        super().save(*args, **kwargs)

    # objects = CustomerManager()

    def __str__(self):
        return self.user.username if self.user else f'{self.phone}'

    class Meta:
        ordering = ('-created',)
        verbose_name = _('Partner')
        verbose_name_plural = _('Partners')
