from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, UserProfile

from allauth.socialaccount.adapter import get_adapter
from allauth.account.admin import get_adapter

from allauth.account.admin import EmailConfirmationAdmin

from allauth.account.models import EmailAddress, EmailConfirmation

class VerifiedEmail(admin.ModelAdmin):
    list_display = ("email", "user", "username", "phone", "primary", "verified")
    list_filter = ("primary", "verified")
    search_fields = []
    raw_id_fields = ("user",)
    actions = ["make_verified"]

    def get_search_fields(self, request):
        base_fields = get_adapter(request).get_user_search_fields()
        return ["email"] + list(map(lambda a: "user__" + a, base_fields))

    def make_verified(self, request, queryset):
        queryset.update(verified=True)

    make_verified.short_description = "Mark selected email addresses as verified"
    
    @admin.display(ordering='phone', description='phone')
    def phone(self, obj):
        # neat trick which can be used on Foreginkey relationships, note that obj.(foreignkeytable).(foreginkeyfield)
        return obj.user.phone

    @admin.display(ordering='username', description='username')
    def username(self, obj):
        # neat trick which can be used on Foreginkey relationships, note that obj.(foreignkeytable).(foreginkeyfield)
        return obj.user.username


# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ('email','is_staff', 'is_active','is_internal')
#     list_filter = ('email', 'is_staff', 'is_active','is_internal')
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Permissions', {'fields': ('is_staff', 'is_active', 'is_internal')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)


admin.site.register(CustomUser)
admin.site.register(UserProfile)
admin.site.unregister(EmailAddress)
admin.site.register(EmailAddress, VerifiedEmail)