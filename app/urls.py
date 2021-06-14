from django.urls import path
from . import views

urlpatterns = [
     path('cod',views.fncod),
     path('file',views.fnfile)
]