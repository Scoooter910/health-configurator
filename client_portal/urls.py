from django.contrib import admin
from django.urls import path
from configurator import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.config_form, name='config_form'),        
    path('success/', views.success_page, name='success'),    
    path('upload/', views.upload_csv, name='upload_csv'),

]

