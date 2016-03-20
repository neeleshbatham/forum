from django.conf.urls import include, url, patterns


urlpatterns =[
    url(r'^$', 'article.views.articles'),
    url(r'^all/$', 'article.views.articles'),
    url(r'^get/(?P<question_id>\d+)/$', 'article.views.article'),
    url(r'^create/$', 'article.views.create'),
    url(r'^search/$','article.views.search_title'),
    url(r'^like/(?P<article_id>\d+)/$', 'article.views.like_article'),
    ]