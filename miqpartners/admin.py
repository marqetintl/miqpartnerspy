from django.contrib import admin

from .models import Partner


class PartnerModelAdmin(admin.ModelAdmin):
    list_display = (
        'last_name', 'first_name', 'phone',
        'email', 'ig', 'tt', 'extra', 'slug'
    )


admin.site.register(Partner, PartnerModelAdmin)
