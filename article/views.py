from django.shortcuts import render_to_response
from django.template import Context
from django.template.loader import get_template
from article.models import Article
#from forms import ArticleForm
#from forms import CommentForm
from django.conf.urls import patterns, include, url
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
import operator
from django import forms
import ipdb

# Create your views here.
def articles(request):
	# ipdb.set_trace()
	return render_to_response('articles.html',
		{'spl_article':Article.objects.get(id=1),
		'articles':Article.objects.all()[:4]})

def article(request, question_id=1):
	return render_to_response('article.html',{'article':Article.objects.get(id=question_id) })

def create(request):
	if request.POST:
		form = ArticleForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/articles/all')
	else:
		form = ArticleForm()

	args ={}
	args.update(csrf(request))

	args['form'] = form

	return render_to_response('create_article.html',args)

##SEARCHING

def search_title(request):
	if request.method == 'GET':
		search_text = request.GET['search_text']
	else:
		search_text = ''

	articles = Article.objects.filter(title__contains=search_text)

	return render_to_response('search.html',{'articles':articles})

def like_article(request,article_id):
	if article_id:
		a = Article.objects.get(id=article_id)
		count = a.likes
		count +=1
		a.likes = count
		a.save()

	return HttpResponseRedirect('/articles/get/%s' % article_id)
