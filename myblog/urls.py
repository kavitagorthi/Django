from django.urls import path
from .views import stub_view
from .views import list_view

urlpatterns = [
    path('',stub_view,name = "blog_index"),
    path('posts/', stub_view, name="blog_detail"),
    path('',list_view,name ="blog_index"),
]