from .views import home_view,SaleListView
from django.urls import path,include

app_name='sales' 

urlpatterns =[
    path('',home_view,name='home'),
    path('list/',SaleListView.as_view(),name='list'),
    ]


