from django.db import models
# from hotelsapp.models import Hotel

# # Create your models here
# evntid(primarykey)

class HoliDetail(models.Model):
    
    event_name = models.CharField(max_length=50)
    holi_event_date = models.CharField(max_length=50,default = '11/11/2019')
    date_for_goa_to_goa = models.CharField(max_length=50,default = '11/11/2019')
    start_from = models.CharField(max_length=100,default="Delhi",blank=True)
    duration = models.CharField(max_length=50,default=0,blank=True)
    mode_of_transport = models.CharField(max_length=20,default="Train",blank=True)
    price = models.DecimalField(default='0',decimal_places=2,max_digits=7,blank=False)
     # event_img = models.ImageField(upload_to='uploadimage')
    quad_with_travel =models.DecimalField(default='0',decimal_places=2,max_digits=7,blank=False) 
    triple_with_travel = models.DecimalField(default='0',decimal_places=2,max_digits=7,blank=False)
    double_with_travel = models.DecimalField(default='0',decimal_places=2,max_digits=7,blank=False)
    quad_wout_travel = models.DecimalField(default='0',decimal_places=2,max_digits=7,blank=False)
    triple_wout_travel = models.DecimalField(default='0',decimal_places=2,max_digits=7,blank=False)
    double_wout_travel = models.DecimalField(default='0',decimal_places=2,max_digits=7,blank=False)
    offer = models.BooleanField(default=False)
    
    def __str__(self):
        return self.event_name

# beach goa party
class BeachDetail(models.Model):
        
    event_name = models.CharField(max_length=50)
    goa_event_date = models.CharField(max_length=50,default = '11/11/2019')
    date_for_goa_to_goa = models.CharField(max_length=50)
    start_from = models.CharField(max_length=100,default="Delhi",blank=True)
    duration = models.CharField(max_length=50,default=0,blank=True)
    mode_of_transport = models.CharField(max_length=20,default="Train",blank=True)
    price = models.DecimalField(default='0',decimal_places=2,max_digits=7,blank=False)
    # event_img = models.ImageField(upload_to='uploadimage')
    quad_with_travel =models.DecimalField(default='0',decimal_places=2,max_digits=7,blank=False) 
    triple_with_travel = models.DecimalField(default='0',decimal_places=2,max_digits=7,blank=False)
    double_with_travel = models.DecimalField(default='0',decimal_places=2,max_digits=7,blank=False)
    quad_wout_travel = models.DecimalField(default='0',decimal_places=2,max_digits=7,blank=False)
    triple_wout_travel = models.DecimalField(default='0',decimal_places=2,max_digits=7,blank=False)
    double_wout_travel = models.DecimalField(default='0',decimal_places=2,max_digits=7,blank=False)
    offer = models.BooleanField(default=False)
    
    def __str__(self):
        return self.event_name

# class PackageDetail(models.Model):
#     # EVENT NAME
#     trip_name = models.CharField(max_length=50)
#     # EVENTS DATE IS FIXED
#     trip_date = models.DateField()
#     #EVENT PRIZE
#     trip_price =models.DecimalField(default='0',decimal_places=2,max_digits=7,blank=False)
#     offer = models.BooleanField(default=False)
#     trip_img = models.ImageField(upload_to='uploadimage',blank=True)
#     trip_from = models.CharField(max_length=100,default="Delhi",blank=True)
#     trip_duration = models.CharField(max_length=50,default=0,blank=True)
#     trip_mode = models.CharField(max_length=20,default="Train",blank=True)
#     choice =(
#             ('family',"FAMILY"),
#             ('luxary',"LUXARY"),
#             ('budget',"BUDGET"),
#             ("college",'COLLEGETRIP'),
#              )
#     package_type = models.CharField(max_length=32,choices=choice,default="family",blank=True)   
#     def __str__(self):
#         return self.trip_name

# class PackageType(models.Model):
#     # packagefk - gripuptrip
#     choice =(
#             ('family',"FAMILY"),
#             ('luxary',"LUXARY"),
#             ('budget',"BUDGET"),
#             ("college",'COLLEGETRIP'),
#     )
#     package_type = models.CharField(max_length=32,choices=choice,default="family")
#     package_name = models.CharField(max_length=32)
#     package_date = models.DateField()
#     package_price =models.DecimalField(default='0',decimal_places=2,max_digits=7,blank=False)
#     offer = models.BooleanField(default=False)
#     package_img = models.ImageField(upload_to='uploadimage')
    
#     def __str__(self):
#         return (self.package_type)
# hotelid(fk/onetoone)        