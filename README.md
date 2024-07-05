# DjangoSimpleBlogApp
Deployed here: http://danielpalacz.pythonanywhere.com/

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
```


### blog application
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

### login application (DjangoUserLoginAuth)
 - usage of basic Django login / logout functionalities
 - django.contrib.auth.views.LoginView
 - django.contrib.auth.views.LogoutView
```
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