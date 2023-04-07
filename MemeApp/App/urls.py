from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('About/',views.About,name="About"),
    path('create/',views.create,name="create"),
    path('editmeme/',views.editmeme,name="editmeme"),
    path('memeDeatails/',views.memeDeatails,name="memeDeatails"),
]

























