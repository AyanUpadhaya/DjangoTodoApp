from django.contrib import admin
from django.urls import path
from . import views
from .views import UpdateView
urlpatterns = [
    path('',views.home,name='home'),
    path('task-delete/<int:id>',views.delete_task,name='task-delete'),
    path('update/<int:pk>',UpdateView.as_view(),name='update'),
   
]
