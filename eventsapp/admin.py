from django.contrib import admin

from .models import HoliDetail,BeachDetail
# from .models import PackageDetail,PackageType
# Register your models here.
admin.site.register(HoliDetail)
admin.site.register(BeachDetail)
# admin.site.register(PackageDetail)
# admin.site.register(PackageType)