from django.contrib import admin
from Contact.models import User_Contact, Instructor_Contact, Payment

# Register your models here.

class User_Contact_Admin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "message", "created_at"]

class Instructor_Contact_Admin(admin.ModelAdmin):
    list_display= ["first_name","last_name","email","phone","degree","subject","address","terms_accepted","created_at"]    

class Payment_Admin(admin.ModelAdmin):
    list_display= ["user","course_name","amount","payment_intent_id","status","created_at"]    
   

admin.site.register(User_Contact, User_Contact_Admin)  
admin.site.register(Instructor_Contact, Instructor_Contact_Admin)   
admin.site.register(Payment, Payment_Admin) 

