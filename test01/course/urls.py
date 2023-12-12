from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'), #1
    path('search/',searches,name='search'), #2
    path('edit/course/<int:id>/',update,name='edit'),
    path('delete/',delete,name='delete'),
]