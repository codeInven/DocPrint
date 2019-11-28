from django.urls import path 
from django.conf.urls import url

from shop import views
app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
     

]