from django.urls import path

from apps.Event import views


urlpatterns = [
    path("register/", views.EventCreateView.as_view(), name="create-event")
    ]