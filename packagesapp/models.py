from django.db import models

# Create your models here.
# trip_id(primary)
# trip-date
# trip-price
# trip_img
# package-id(foreign/onetoone)
class PackageDetail(models.Model):
    
    # EVENT NAME
    trip_name = models.CharField(max_length=50)
    # EVENTS DATE IS FIXED
    trip_date = models.DateField()
    # CEVENT PRIZE
    trip_price =models.DecimalField(default='0',decimal_places=2,max_digits=7,blank=False)
    offer = models.BooleanField(default=False)
    trip_img = models.ImageField(upload_to='uploadimage',blank=True)
    trip_from = models.CharField(max_length=100,default="Delhi")
    trip_duration = models.CharField(max_length=50,default=0,blank=True)
    trip_mode = models.CharField(max_length=20,default="Train",blank=True)
    choice =(
            ('family',"FAMILY"),
            ('luxary',"LUXARY"),
            ('youth',"YOUTH"),
            )
    package_type = models.CharField(max_length=32,choices=choice,default="family",blank=True)   
    def __str__(self):
        return self.trip_name

class PackageType(models.Model):
    # packagefk - gripuptrip
    choice =(
            ('family',"FAMILY"),
            ('luxary',"LUXARY"),
            ('youth',"YOUTH"),
            )
    package_type = models.CharField(max_length=32,choices=choice,default="family")
    package_name = models.CharField(max_length=32)
    package_date = models.DateField()
    package_price =models.DecimalField(default='0',decimal_places=2,max_digits=7,blank=False)
    offer = models.BooleanField(default=False)
    package_img = models.ImageField(upload_to='uploadimage')
    
    def __str__(self):
        return (self.package_type)
# hotelid(fk/onetoone)