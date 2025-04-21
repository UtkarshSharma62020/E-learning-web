from django.contrib import admin
from Contact.models import User_Contact

# Register your models here.

class User_Contact_Admin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "message", "created_at"]
   

admin.site.register(User_Contact, User_Contact_Admin)   

