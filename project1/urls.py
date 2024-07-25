"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from todo.views import home, todo_detail, category_detail, tag_view
from project1.views import logout_view

urlpatterns = [
    path("", home),
    path("category/<slug:category_slug>/todo/<int:id>", todo_detail, name="todo_detail_name"),
    path("category/<slug:category_slug>", category_detail, name="category_detail_name"),
    path("tag/<slug:tag_slug>", tag_view, name="tag_view_name"),
    #path("todo/<int:id>", todo_detail_2, name="todo_detail"),
    path("logout/", logout_view, name="logout_view"),
    path("admin/", admin.site.urls),
]
