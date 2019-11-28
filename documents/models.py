from django.db import models

# Create your models here.
class files(models.Model):
    #name,extension,pages
    #title,pages,user_id
     
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='documents/media/doc/')
    size = models.CharField(max_length=255, blank=True)
    F_type = models.CharField(max_length=255, blank=True)
    pages = models.CharField(max_length=255, blank=True)
    user_id = models.IntegerField(  blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title  
    class Meta:  
        db_table = "files"
        verbose_name_plural = "files"
        
 
class Binding(models.Model):
    name = models.CharField(max_length=255, blank=True)
    detail = models.CharField(max_length=1024, blank=True)
    price = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='documents/media/binding/')
    def __str__(self):
        return self.name  
class Meta:  
    db_table = "Binding"
    verbose_name_plural = "Binding"

'''
class BindingProfile(models.Model):'''

