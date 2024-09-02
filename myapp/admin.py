from django.contrib import admin
from .models import Enquiry,Blog

# Register your models here.

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject','message']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','image','title','description','date']

