from django.conf.urls import url
from . import views


urlpatterns = [

          url('python/', views.pythonlang, name='python'),
          url(r'^python_overview/(?P<page>[0-9]+)/$', views.python_overview, name='python_overview')

    ]