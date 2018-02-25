from django.conf.urls import url
from . import views
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf import settings
#from companies import views as core_views
from rest_framework.urlpatterns import format_suffix_patterns

app_name='companies'
urlpatterns = [
url(r'^index/$',views.index,name='index'),
url(r'^post/new/$', views.transport_new, name='post_new'),
url(r'^detail/(?P<album_id>[0-9]+)/$', views.StockList1.as_view(), name='detail'),
url(r'^albdetail/(?P<album_id>[0-9]+)/$', views.albdetail, name='albdetail'),
url(r'^test/$', views.test, name='test'),
url(r'^service/$', views.service, name='service'),
url(r'^team/$', views.team, name='team'),
url(r'^problems/$', views.problems, name='problems'),
url(r'^contact/$', views.contact, name='contact'),
url(r'^login/$', views.login, name='login'),
url(r'^rregister/$', views.rregister, name='rregister'),
url(r'^register/$', views.register, name='register'),
url(r'^login1/$', views.Login1copy.as_view(), name='login1_new'),
url(r'^loginc/$', views.Logincopy.as_view(), name='loginc_new'),
url(r'^email_verify/(?P<emailto>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/',views.email_verify, name='email_verify'),
url(r'^deid/$', views.StockList0.as_view(), name='deid'),
url(r'^$',views.home, name='home'),
url(r'^login2/$', auth_views.login, {'template_name': 'companies/login.html'}, name='login2'),
url(r'^logout/$', auth_views.logout, {'next_page': 'companies:login2'}, name='logout'),
url(r'^signup/$', views.signup, name='signup'),
url(r'^display/(?P<getPid>\d+)/$',views.display,name='display'),
url(r'^delete/(?P<getPid>\d+)/$', views.deleteProblem, name='deleteProblem'),
url(r'^update/$', views.updateStatus, name='update'),
url(r'^ser/$',views.ProbList.as_view()),
]


