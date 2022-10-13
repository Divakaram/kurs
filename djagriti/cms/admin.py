from django.contrib import admin

# Register your models here.
from cms.models import *


class TeacherAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(CmsSlider)
admin.site.register(CmsTeachers, TeacherAdmin)
