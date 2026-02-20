from django.contrib import admin 
from .models import Students

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'state', 'phone', 'joined_date')
    
admin.site.register(Students, StudentAdmin)