from django.urls import path 
from django.conf.urls import url
from documents import views
app_name = 'documents'
urlpatterns = [
    path('', views.index, name='index'),
    path('panel', views.panel, name='index'),
    path('table.html', views.table, name='table.html'),
    
     

]