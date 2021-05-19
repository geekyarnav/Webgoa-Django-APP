from django.db import models
# from eventsapp.models import Customer
# # Create your models here.
# class Hotel(models.Model):
#     H_Id        = models.AutoField(primary_key=True,null=False,unique=True)
#     H_Name      = models.CharField(max_length=30,blank=False)
#     H_Image     = models.ImageField(upload_to='uploadimage',default=None)
#     H_Price     = models.DecimalField(decimal_places=2,max_digits=100)
#     Cust_Id     = models.OneToOneField(Customer,on_delete=models.CASCADE)
#     #Facility = rest
#     Check_In    = models.DateField()
#     Check_Out   = models.DateField()
    
#     def __str__(self):
#         return self.H_Name    
    

# class Customer(models.Model):
#     # RANDOM
#     # id primary auto increatment
#     # Customer_id = models.AutoField(primary_key=True)
#     #  ERROR - Integrity  errror- Unique.constraint.failed  
#    
#  Customer_Id        = models.AutoField(primary_key=True,null=False,unique=True)
#     # Customer_Id = models.IntegerField(unique=True,blank=False,null=False)
# 
#     Full_Name   = models.CharField(max_length=30,blank=False,null=False,default='James Bond')
#     City        = models.CharField(max_length=10,default='NewYork')
#     Mob_No      = models.PositiveIntegerField(default=0)
# 
#     # Hotel     = models.ManyToManyField(Hotel)
#     # on_delete=models.CASCADE
#     # E_Mail      = models.EmailField(unique=True,
#                     # default='xyz@mail.com',
#                     # blank=False,null=False
#                     # validators=)    
    # def __str__(self):
#         return self.Full_Name -->
    