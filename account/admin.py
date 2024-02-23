from django.contrib import admin

from account.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ("name", "active")
    actions = ["activate_accounts", "deactivate_accounts"]

    @admin.action(description="Activate selected accounts")
    def activate_accounts(self, request, queryset):
        queryset.update(active=True)

    @admin.action(description="Deactivate selected accounts")
    def deactivate_accounts(self, request, queryset):
        queryset.update(active=False)


# Register your models here.
admin.site.register(Account, AccountAdmin)
