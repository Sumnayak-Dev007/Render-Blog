from django.contrib import admin
from .models import UserPost,Comments,Category,Catblog,Contact
# Register your models here.

class UserPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at') 


admin.site.register(UserPost,UserPostAdmin)
admin.site.register(Comments)
admin.site.register(Category)
admin.site.register(Catblog)
admin.site.register(Contact)