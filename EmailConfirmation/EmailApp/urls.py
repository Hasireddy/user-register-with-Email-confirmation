from django.urls import path

from django.conf import settings

from django.conf.urls.static import static

from . import views

app_name = "EmailApp"

urlpatterns = [
    path("register/", views.user_register, name="register"),
    path("confirm/<user_id>/<token>", views.confirm_email, name="confirm_email"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
