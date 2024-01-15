from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('personal', views.personal),
    path('coding', views.coding),
    path('best', views.best)
]

