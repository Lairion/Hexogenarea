from django.shortcuts import render
from .models import ListMaster

# Create your views here.
def main_window(request):
    list_master = ListMaster.objects.all()
    title = "list"
    context = {
        "title":title,
        "list_master":list_master
    }