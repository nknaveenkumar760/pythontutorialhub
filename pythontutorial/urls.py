<<<<<<< HEAD
from django.conf.urls import url, include
=======
from django.conf.urls import url
>>>>>>> 2182f3a4b8fdddf73aa0b260257e2d329ad6c815
from . import views


urlpatterns = [

          url('python/', views.pythonlang, name='python'),
<<<<<<< HEAD
          url(r'^python_overview/(?P<page>[0-9]+)/$', views.python_overview, name='python_overview'),
          url('videofile', views.showvideos, name='videofile')
=======
          url(r'^python_overview/(?P<page>[0-9]+)/$', views.python_overview, name='python_overview')
>>>>>>> 2182f3a4b8fdddf73aa0b260257e2d329ad6c815

    ]