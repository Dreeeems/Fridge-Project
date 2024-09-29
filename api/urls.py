from django.contrib import admin
from django.urls import path 
from .views import  ItemList,ItemDetail,ItemCreate,ItemUpdate,ItemDelete,TypeList,TypeDetail,TypeCreate,TypeUpdate,TypeDelete
urlpatterns = [
 path('items/',ItemList.as_view()),
 path('item/<int:pk>',ItemDetail.as_view()),
 path('item/create',ItemCreate.as_view()),
 path('item/<int:pk>/update',ItemUpdate.as_view()),
 path('item/<int:pk>/delete',ItemDelete.as_view()),
 path('types/',TypeList.as_view()),
 path('type/<int:pk>',TypeDetail.as_view()),
 path('type/create',TypeCreate.as_view()),
 path('type/<int:pk>/update',TypeUpdate.as_view()),
 path('type/<int:pk>/delete',TypeDelete.as_view()),
]
