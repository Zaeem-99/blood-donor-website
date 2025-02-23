"""
URL configuration for BloodBank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from Home.views import *
# from .views import search_page, send_email_to_donor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main-page/', main_page , name = 'main-page'),
    path('register-p/', register_p , name = 'register-p'),
    # path('register-page/', register_page , name = 'register-page'),
    path('search-page/', search_page , name = 'search-page'),
    path('send-email/<str:email>', send_email, name='send-email'),
    path('', login_page , name = 'login-page'),
    path('contact-page/', contact_page , name = 'contact-page'),
    path('about-page/', about_page , name = 'about-page'),
      
]


# <str:donor_email>/
