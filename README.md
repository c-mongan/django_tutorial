# django_tutorial

This project follows the official Django tutorial

##Tutorial 1

1) Check if django is installed - ``py -m django --version``

2) Create a project with ``django-admin startproject mysite``

3) Verify the project works with ``py manage.py runserver`` (Must cd to mysite directory first)

#(CTRL + C) to stop server running


4) Visit "http://127.0.0.1:8000/" on your browser to see if it worked

5)If you wish to change the port run ``py manage.py runserver 8080``

6)Create an app called polls by running ``py manage.py startapp polls``

7)Open polls/views.py and paste the following code:

``from django.http import HttpResponse``



``def index(request):``
    ``return HttpResponse("Hello World! You are at the polls index.")``

8) Create a file in the polls directory called "urls.py" so that we can map the index page to it and paste the code below:

``from django.urls import path``
``from . import views``

``urlpatterns = [``
    ``path('', views.index, name='index'),``
``]``

9) Now in mysite/urls paste the following

``from django.contrib import admin``
```from django.urls import include, path```

``urlpatterns = [``
    ``path('polls/', include````('polls.urls')),``
   `` path('admin/', admin.site.urls),``
``]``

10) Now run
``...\> py manage.py runserver``

11)Navigate to ``http://localhost:8000/polls/``

##Tutorial 2

##Tutorial 3

##Tutorial 4

##Tutorial 5