"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from app.views.index import index, add_comment
from app.views.comments.admin import admin, approve_comment, deny_comment

urlpatterns = [
    path("", index, name="index"),
    path('admin/', admin, name='admin'),
    
    # API
    path("add_comment/", add_comment, name="add_comment"),
    path("approve_comment/", approve_comment, name="approve_comment"),
    path("deny_comment/", deny_comment, name="deny_comment"),
]

