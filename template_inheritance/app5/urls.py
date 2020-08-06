from django.urls import path,include
from app5 import views

app_name = "app5"

urlpatterns = [
    path('other/', views.other, name="other"),
    path('relative', views.relative, name="relative"),
]
