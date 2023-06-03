from django.urls import path

from apps.Registration import views

urlpatterns = [
    path("register/", views.RegistrationCreateView.as_view(), name="register-event"),
    path("list/", views.UserRegistrationListAPIView.as_view(), name="registration-list"),
]