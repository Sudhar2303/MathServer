from django.contrib import admin
from django.urls import path
from app5 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('areaofrectangle/',views.prismarea,name="areaofrectangle"),
    path('',views.prismarea,name="areaofrectangleroot")
]