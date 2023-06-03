from django.urls import path

from apps.Event import views


urlpatterns = [
    path("register/", views.EventCreateView.as_view(), name="create-event"),
    path("list/", views.EventListView.as_view(), name="list-events"),
    path("detail/<int:pk>/", views.EventDetailView.as_view(), name="detail")
]