from django.contrib import admin
from .models import *

# Register your models here.

class ProfileAdminModel(admin.ModelAdmin):
    list_display = ('name','verified')
    search_fields = ('user__first_name','user__last_name','user__username',)
    list_display_links=('name', 'verified')
    
    
    def name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name} {obj.user.username}"
    
    @admin.display(description="IS VERIFIED", boolean=True)
    def verified(self, obj):
        return obj.is_email_verified
    
        

admin.site.register(Profile, ProfileAdminModel)
