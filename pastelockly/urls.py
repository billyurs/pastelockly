"""pastelockly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import app.views

urlpatterns = [
    url(r'^$', app.views.index),
    url(r'^sender$', app.views.sender),
    url(r'^receiver', app.views.receiver),
    url(r'^admin/', admin.site.urls),
    url(r'^save_sender_data$', app.views.save_sender_data),
    url(r'^decode_sender_data$', app.views.decode_sender_data),
]
