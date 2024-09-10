from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name='index'),
    path("delete/<int:pk>/", delete, name="delete"),
    path("update/<int:pk>/", update, name="update")
]
