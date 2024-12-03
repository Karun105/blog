from django.urls import path
from blogapp import views

app_name = "blogapp"

urlpatterns = [
    path("",views.index, name="index"),
    path("blog/<str:slug>",views.detail, name="detail"),
    path("new_url/",views.new_url_detail, name="new_page_url"),
    path("old_url/",views.old_url_detail, name="old_url"),
    
]