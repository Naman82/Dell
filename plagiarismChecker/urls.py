from django.urls import path
from . import views

urlpatterns=[
    path('upload/',views.FileUploder.as_view(),name="fileupload"),
]