from django.conf.urls import include, url
from . import views

urlpatterns = [
url(r'^$', views.splash, name='splash'),
url(r'^home$', views.index, name='index'),
url(r'^language$', views.language, name='language'),
url(r'^healthpass$', views.healthpass, name='healthpass'),
url(r'^submitanswer$', views.submitanswer, name='submitanswer'),
url(r'^question_(\d+).html$', views.question, name='question'),
url(r'^personal$', views.personal, name='personal'),
url(r'^yourhome$', views.yourhome, name='yourhome'),
]
