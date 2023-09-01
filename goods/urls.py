from django.urls import path
from .views import detail, all

urlpatterns=[
    path('all/', all),
    path('detail/<int:myid>', detail)
]