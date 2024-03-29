"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from tree import views as treeViews
from user import views as userViews

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", userViews.user_login, name="login"),
    path("index/", userViews.dashboard, name="dashboard"),
    # <-- API -->
    path("api/planted_tree/", treeViews.PlantedTreeList.as_view()),
]
