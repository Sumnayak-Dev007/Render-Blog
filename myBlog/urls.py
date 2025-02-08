from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('post_view/<int:pk>/',views.post_view,name="post_view"),
    path('post_edit/<int:pk>/',views.post_edit,name="post_edit"),
    path('post_del/<int:pk>/',views.post_del,name="post_del"),
    path('your_post/',views.your_post,name="your_post"),
    path("search/", views.search_results, name="search_results"), 
    path('category/<str:slug>',views.category_view,name="category_view"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('base/',views.baseeee,name="base"),
]