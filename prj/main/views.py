from django.shortcuts import render
from main.models import Server

def get_homepage(request):
    context = {
        "servers": Server.objects.all().order_by("title")
    }
    return render(request, "main/homepage.html", context)
# Create your views here.
