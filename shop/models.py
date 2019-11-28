from django.db import models

# Create your models here.

class Shops(models.Model): 
    #fs_img = FileSystemStorage(location='media/images')
    #        fs_pic = FileSystemStorage(location='media/pictures')  
   
    opperator_name      = models.CharField('Opperator Name',max_length=50)  
    Shop_name   = models.CharField('Shop Name',max_length=100)  
    address = models.FileField('Address',upload_to = 'pictures/')
    location=models.CharField('Location',max_length=250)  
    city=models.CharField('City',max_length=250)  

    def __str__(self):
        return self.opperator_name  
    class Meta:  
        db_table = "shops"
        verbose_name_plural = "shops"
class Agrement(models.Model):
     
    Shop = models.ForeignKey(Shops, null=True,on_delete=models.CASCADE)
    agrement_details=models.TextField('Agrement',max_length=4096)
    def __str__(self):
        return self.agrement_details  
    class Meta:  
        db_table = "agrement"
        verbose_name_plural = "Agrement"
'''
class Printerlist(models.Model):
    manufacture=
    model=
    color_type=
    quantity=
class printer(models.Model):
    pid,shopid,accountid'''