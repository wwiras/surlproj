from django.conf.urls import include,url
from . import views
from django.urls import path

urlpatterns = [

    # CRUD course
    path('list/',views.myurl_list,name='myurl_list'),
    path('create/',views.myurl_create,name='myurl_create'),
]
