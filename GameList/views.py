from django.shortcuts import render
from .models import ListMaster
from django.contrib.auth.models import User

# Create your views here.
def main_window(request):
    list_master = ListMaster.objects.all()
    title = "list"
    list_name = User.objects.all()
    context = {
        "title":title,
        "list_master":list_master,
        "list_name":list_name
    }
    return render(request,"main.html",context)
