from django.contrib import admin

# Register your models here.
from .models import Lawyer  # , UserProfile

admin.site.site_header = "Muigua & Co Advocates"
admin.site.site_title = "Muigua & Co Advocates"
admin.site.index_title = "SETTINGS"
admin.AdminSite.index_title = "ADMIN DASHBOARD"


class LawyerAdmin(admin.ModelAdmin):
    search_fields = ('lawyer_name', 'lawyer_email', 'lawyer_mobile',)
    list_display = ('lawyer_email', 'lawyer_name', 'lawyer_mobile', 'lawyer_experience',)


# class UserProfileAdmin(admin.ModelAdmin):
#     search_fields = ('user', )
#     list_display = ('user', 'case', 'case_description', )


admin.site.register(Lawyer, LawyerAdmin)
# admin.site.register(UserProfile, UserProfileAdmin)
