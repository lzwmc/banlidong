from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,"register.html")
def home(request):
    return render(request,"home.html")
def zs(request):
    return render(request,"zs.html")
def updata(request):
    return render(request,"updata.html")
def pz(request):
    return render(request,"pz.html")
def gz(request):
    return render(request,"gz.html")
def ban(request):
    return render(request,"ban.html")
def gl(request):
    return render(request,"gl.html")