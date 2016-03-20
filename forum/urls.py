"""forum URL Configuration

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
from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^articles/', include('article.urls')),
    url(r'^$', include('article.urls'))


    #Authentication Urls
    #url(r'^accounts/login/$', 'forum.views.login'),
    #url(r'^accounts/auth/$', 'forum.views.auth_view'),
    #url(r'^accounts/logout/$', 'forum.views.logout'),
    #url(r'^accounts/loggedin/$', 'forum.views.loggedin'),
    #url(r'^accounts/invalid/$', 'forum.views.invalid_login'),

    #Register Urls
    #url(r'^accounts/register/$', 'forum.views.register_user'),
    #url(r'^accounts/register_success/$', 'forum.views.register_success'),
]
handler500 = 'articles.views.handler500'