from django.urls import path
from .views import getall, postall, detail

urlpatterns=[
    path('all/', getall.as_view()),
    path('detail/<int:myid>', detail),
    path('create/>', postall.as_view() )
]