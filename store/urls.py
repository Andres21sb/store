#import path
from django.urls import path
#import views
from . import views
#URLConf
urlpatterns=[
    path('hello/',views.say_store)
]