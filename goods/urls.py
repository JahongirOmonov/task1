from django.urls import path
from .views import GetAllFirst, PostFirst, GetDetailFirst, PatchFirst, DeleteFirst, AllFunctionFirst, PostGetFirst
from .views import GetAllSecond, GetDetailSecond, PostSecond, PatchSecond, DeleteSecond, AllFunctionSecond, PostGetSecond

urlpatterns=[
    path('GetAllFirst/', GetAllFirst.as_view()),
    path('GetDetailFirst/<int:pk>', GetDetailFirst.as_view()),
    path('PostFirst/', PostFirst.as_view() ),
    path('PatchFirst/<int:pk>', PatchFirst.as_view()),
    path('DeleteFirst/<int:pk>', DeleteFirst.as_view()),
    path('PostGetFirst/', PostGetFirst.as_view()),
    path('AllFunctionFirst/<int:pk>', AllFunctionFirst.as_view()),
    path('GetAllSecond/', GetAllSecond.as_view()),
    path('GetDetailSecond/<int:pk>', GetDetailSecond.as_view()),
    path('PostSecond/', PostSecond.as_view() ),
    path('PatchSecond/<int:pk>', PatchSecond.as_view()),
    path('DeleteSecond/<int:pk>', DeleteSecond.as_view()),
    path('PostGetSecond/', PostGetSecond.as_view()),
    path('AllFunctionSecond/<int:pk>', AllFunctionSecond.as_view())


]