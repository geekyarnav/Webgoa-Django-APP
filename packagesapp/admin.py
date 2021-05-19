from django.contrib import admin
from .models import PackageDetail,PackageType
# Register your models here.
admin.site.register(PackageType)
admin.site.register(PackageDetail)