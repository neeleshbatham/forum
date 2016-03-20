from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib import auth
from forms import MyRegistrationForm

def home(request):
	display = "This is Home Page"
	html = "<html><h1> %s </h1></html>" % display
	return HttpResponse(html)


def login(request):
	c={}
	c.update(csrf(request))	
	return render_to_response('login.html',c)

def invalid_login(request):
	return render_to_response('invalid_login.html')


def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username,password=password)

	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
	return render_to_response('loggedin.html', {'full_name':request.user.username})

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')

def register_user(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/register_success')
	
	args = {}
	args.update(csrf(request))
 
	args['form'] = MyRegistrationForm()

	return render_to_response('register.html',args)


def register_success(request):
	return render_to_response('register_success.html')


