from django.shortcuts import render, HttpResponse

from django.contrib.auth.hashers import make_password

from .forms import UserRegisterForm

# Create your views here.

# def user_register(request):
#     if request.method == "POST":
#         form = UserRegisterForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("user registered")
#     else:
#         form = UserRegisterForm()
#     return render(request,"EmailApp/register.html",{"register_form":form})


def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            # Hashing Password before saving it to the database
            user.password = make_password(user.password)
            user.save()
            return HttpResponse("success")

    else:
        form = UserRegisterForm()
    return render(request, "EmailApp/register.html", {"register_form": form})
