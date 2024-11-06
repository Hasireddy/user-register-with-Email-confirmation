from django.shortcuts import render, HttpResponse, redirect

from django.contrib.auth.hashers import make_password

from django.utils.http import urlsafe_base64_decode

from django.contrib.auth.tokens import default_token_generator

from .forms import UserRegisterForm

from .models import User

from .utils import send_confirmation_mail

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
            send_confirmation_mail(request, user)
            return HttpResponse("success")

    else:
        form = UserRegisterForm()
    return render(request, "EmailApp/register.html", {"register_form": form})


# Verifying the confirmation link once user clicks on the confirmation link


def confirm_email(request, user_id, token):
    try:
        id_ = urlsafe_base64_decode(user_id).decode()
        # retrieve the user by their decoded ID.
        user = User.objects.get(id=id_)
    except User.DoesNotExist as err_obj:
        user = None
    # checks if the provided token is valid for the user. If the token matches, it indicates that the link is valid.
    if user is not None and default_token_generator.check_token(user, token):
        # Verify the user account when he clicks on the verification link and activate it.
        user.is_active = True
        user.save()
        return redirect("EmailApp:register")
    else:
        messages.error(request, "Invalid link1")
        return redirect("EmailApp:register")
