"""Project_skeleton URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from skeleton.views import home_view, create_view, read_view, list_update_view, list_delete_view, update_view, delete_view, register_view, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('create', create_view),
    path('read', read_view),
    path('update', list_update_view),
    path('update/<int:ids>/', update_view),
    path('delete', list_delete_view),
    path('delete/<int:ids>/', delete_view),
    path('registration', register_view),
    path('login', login_view),
]
