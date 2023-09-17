from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Certification)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','duration']


@admin.register(Enrollment)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['id','user','certification','enrollment_date','completion_date']

@admin.register(CertificateRequest)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['id','user','certification','status']