"""wordcount URL Configuration

The `urlpatterns` list routes URLs to view.py. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function view.py
    1. Add an import:  from my_app import view.py
    2. Add a URL to urlpatterns:  path('', view.py.home, name='home')
Class-based view.py
    1. Add an import:  from other_app.view.py import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', view.about, name='about'),
    path('', view.home, name='home'),
    path('count/', view.count, name='count')
]
