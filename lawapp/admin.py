from django.contrib import admin

# Register your models here.
from .models import Lawyer, Clients, RePresentation, Appearance, Cases, Courts  # , UserProfile

admin.site.site_header = "Muigua & Co Advocates"
admin.site.site_title = "Muigua & Co Advocates"
admin.site.index_title = "Administration"
admin.AdminSite.index_title = "ADMIN DASHBOARD"


class LawyerAdmin(admin.ModelAdmin):
    search_fields = ('lawyer_username', 'lawyer_mobile',)
    list_display = ('lawyer_username', 'lawyer_mobile', 'lawyer_experience', )
    list_display_links = ('lawyer_username', 'lawyer_mobile')
    list_filter = ('lawyer_mobile',)


class ClientsAdmin(admin.ModelAdmin):
    search_fields = ('client_username', 'client_mobile',)
    list_display = ('client_username', 'client_mobile', 'client_age', 'client_party')
    list_display_links = ('client_username', 'client_mobile')
    list_filter = ('client_mobile',)


class CasesAdmin(admin.ModelAdmin):
    search_fields = ('case_title', 'case_unique_key',)
    list_display = ('case_title', 'case_owner_username', 'case_unique_key', 'created_at', 'case_status')
    list_display_links = ('case_title', 'case_unique_key', 'created_at', 'case_status')
    list_filter = ('case_unique_key',)


class RePresentationAdmin(admin.ModelAdmin):
    search_fields = ('Represented_by', 'Represented_user',)
    list_display = ('Represented_by', 'Represented_user', 'presentation_court', 'presented_to',)
    list_display_links = ('Represented_by', 'Represented_user', 'presentation_court', 'presented_to',)
    list_filter = ('Represented_by',)


class CourtsAdmin(admin.ModelAdmin):
    search_fields= ('court_name', 'court_location', 'court_address',)
    list_display = ('court_name', 'court_location', 'court_address', )
    list_display_links = ('court_name', 'court_location', 'court_address', )


class AppearanceAdmin(admin.ModelAdmin):
    search_fields = ('Appearing_lawyer', 'Appearance_court', 'Appearance_date', 'Appearance_status')
    list_display = ('Appearing_lawyer', 'Appearance_court', 'Appearance_date', 'Appearance_status')
    list_display_links = ('Appearing_lawyer', 'Appearance_court', 'Appearance_date', 'Appearance_status')


# class UserProfileAdmin(admin.ModelAdmin):
#     search_fields = ('user', )
#     list_display = ('user', 'case', 'case_description', )


admin.site.register(Lawyer, LawyerAdmin)
admin.site.register(Cases, CasesAdmin)
admin.site.register(Clients, ClientsAdmin)
admin.site.register(RePresentation, RePresentationAdmin)
admin.site.register(Courts, CourtsAdmin)
admin.site.register(Appearance, AppearanceAdmin)

# admin.site.register(UserProfile, UserProfileAdmin)
