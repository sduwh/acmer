from django.contrib import admin
from .models import Code


class CodeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Code, CodeAdmin)
