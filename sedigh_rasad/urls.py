from django.contrib import admin
from django.urls import path
from main.views import main_page
from main.views import export_present_members
from main.views import finish
urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', main_page, name='members'),  
    path('download/',export_present_members, name='download_scv'),
    path('',finish, name='done' )
]