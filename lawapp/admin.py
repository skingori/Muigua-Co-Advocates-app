from django.contrib import admin

# Register your models here.
from .models import Lawyer, Clients, RePresentation, Appearance, Cases  # , UserProfile

admin.site.site_header = "Muigua & Co Advocates"
admin.site.site_title = "Muigua & Co Advocates"
admin.site.index_title = "SETTINGS"
admin.AdminSite.index_title = "ADMIN DASHBOARD"


class LawyerAdmin(admin.ModelAdmin):
    search_fields = ('lawyer_username', 'lawyer_mobile',)
    list_display = ('lawyer_username', 'lawyer_mobile', 'lawyer_experience', )


# class UserProfileAdmin(admin.ModelAdmin):
#     search_fields = ('user', )
#     list_display = ('user', 'case', 'case_description', )


admin.site.register(Lawyer, LawyerAdmin)
admin.site.register(Cases)
# admin.site.register(UserProfile, UserProfileAdmin)
