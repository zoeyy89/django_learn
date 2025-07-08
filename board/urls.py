from django.urls import path
from . import views

app_name = "board"

urlpatterns = [
    path("", views.message_list, name="message_list"),
]
