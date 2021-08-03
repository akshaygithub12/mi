from django.shortcuts import render
from django.views.generic import ListView
from .models import Sales
# Create your views here.
def home_view(request):
    h="hsdjashdjkashdas"
    return render(request,'sales/main.html',{'h':h})


class SaleListView(ListView):
    models=Sales
    template_name='sales/main.html'
    
