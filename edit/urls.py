from django.urls import path
from . import views


urlpatterns = [
    path('modify_plan', views.modify_plan),
]
