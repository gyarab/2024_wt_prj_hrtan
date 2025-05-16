from django.shortcuts import render
from main.models import Server


# Create your views here.
def get_homepage(request):
    servers = Server.objects.all().order_by("price")

    # check if search parameter is in the request
    if request.GET.get("search"):
        servers = servers.filter(title__icontains=request.GET.get("search"))
    
    context = {
        "servers": servers,
    }
    return render(request, "main/homepage.html", context)

