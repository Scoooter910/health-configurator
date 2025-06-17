from django.contrib import admin
from django.urls import path
from configurator import views  # 👈 import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.config_form, name='config_form'),         # 👈 main form page
    path('success/', views.success_page, name='success'),    # 👈 success page
]
