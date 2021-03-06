"""fake_bos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from fake_bos import views

app_name = 'fake_bos'

urlpatterns = [
    url(r'^$', views.login_view, name='login_view'),
    url(r'^admin/', admin.site.urls),
    url(r'^index$', views.index, name='index'),
    url(r'^login$', views.login_view, name='login_view'),
    url(r'^logout$', views.logout_view, name='logout_view'),
    url(r'^register$', views.register_view, name='register_view'),
    url(r'^view_survey/(?P<survey_id>[0-9]+)/$', views.view_survey, name='view_survey'),
    url(r'^response/.*$', views.register_response, name='register_response'),
    #url(r'^response/(?P<id_user>[0-9]+)/(?P<id_question>[0-9]+)/(?P<answer>.+)/$', views.register_response, name='register_response'),
    #url(r'^api/', include('fake_bos.api.urls')),

]
