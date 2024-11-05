from django.shortcuts import render,HttpResponse

from .forms import UserRegisterForm

# Create your views here.

def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("user registered")
    else:       
        form = UserRegisterForm()
    return render(request,"register.html",{"register_form":form})
        


