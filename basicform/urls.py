"""basicform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path,include

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('output', views.add, name='output'),
    path('out', views.cse, name='output'),
    path('outcsr', views.cser, name='output'),
    path('outcsr21', views.csr21, name='output'),
    path('outcsh21', views.csh21, name='output'),
    path('outecer21', views.ecer21, name='output'),
    path('outech21', views.eceh21, name='output'),
    path('outai21', views.aih21, name='output'),
    path('outair21', views.air21, name='output'),
    path('outec20', views.ec20, name='output'),
    path('outfed', views.fed, name='output'),
    path('',include('cal.urls')),

]
