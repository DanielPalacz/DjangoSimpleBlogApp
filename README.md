# DjangoSimpleBlogApp
```
Developed home page app endpoints:
	GET /
	GET projects/
	GET contact/
	GET account/
	 - dashboard page (login required)
	GET api-info/
	 - dashboard page (login required)


Developed 'blog' app endpoints:
	GET /blog
	GET /blog/<post_slug_id>
```

# DjangoUserLoginAuth
 - login app
 - usage of basic Django login / logout functionalities
 - django.contrib.auth.views.LoginView
 - django.contrib.auth.views.LogoutView
```
python -m venv venv
source venv/bin/activate
pip install Django

django-admin startproject mysite
cd mysite
python manage.py startapp login
	register 'login' application

Developed html templates
 - login.html
 - user_logged_out.html
 - dashboard.html
 
settings.py:
	LOGIN_REDIRECT_URL = "/account/"
	LOGOUT_REDIRECT_URL = "/logged_out/"
	LOGIN_URL = "/login/"
	LOGOUT_URL = "/logout/"

Developed 'login' app endpoints:
	GET /login
	POST /logout
	GET /logged_out
	GET /account
		- dashboard page
```