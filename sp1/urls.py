"""sp1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from sp1 import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),


	url(r'^saml2/logout/$', views.my_saml_logout, name='my_saml_logout'),

    url(r'^saml2/', include('djangosaml2.urls')),
	url(r'^test/', 'djangosaml2.views.echo_attributes'),

	url(r'^$', views.view_profile, name='home'),
    url(r'^accounts/profile/', views.view_profile, name='view_profile'),

]
