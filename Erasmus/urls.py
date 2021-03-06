from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views
from blog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
	url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
	url(r'^temas/$', views.lugarlist, name='lugares'),
    url(r'^temas/(?P<pk>\d+)/$', views.lugar_topics, name='temas_lugar'),
    url(r'^temas/(?P<pk>\d+)/Restaurantes/$', views.Restaurantelist, name='restaurantes'),
    url(r'^temas/Restaurantes/new/$', views.new_restaurante, name='newrestaurante'),
	url(r'^admin/', admin.site.urls),	
	url(r'^reset/$',auth_views.PasswordResetView.as_view(template_name='password_reset.html',email_template_name='password_reset_email.html',subject_template_name='password_reset_subject.txt'),name='password_reset'),
	url(r'^reset/done/$',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    url(r'^reset/complete/$',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
]