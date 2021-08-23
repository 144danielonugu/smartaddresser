from django.shortcuts import render,get_object_or_404,redirect
from addressapp.models import address
from django.contrib.auth.models import User,auth
# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    if request.method=="POST":
        username=request.POST["user"]
        passcode=request.POST["codepass"]
        user=auth.authenticate(username=username,password=passcode)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
    return render(request,'login.html')
    return render(request,'login.html')
def addresslist(request):
    obj=address.objects.all()
    return render(request,'addresslist.html',{'objs':obj})
def addressmain(request,id):
    obj=get_object_or_404(address,id=id)
    return render(request,'addressmain.html',{'objs':obj})
def logout(request):
    auth.logout(request)
    return redirect("home")