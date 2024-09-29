from django.contrib import admin
from django.urls import path 
from .views import  ItemList,ItemDetail, TypeList,TypeDetail
urlpatterns = [
 path('items/',ItemList.as_view()),
 path('item/<int:pk>',ItemDetail.as_view()),
 path('types/',TypeList.as_view()),
 path('type/<int:pk>',TypeDetail.as_view()),
]
