from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from website.forms import MyLoginForm, MyPasswordReset, MyPasswordChangeForm


urlpatterns = patterns('',
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'website.views.index', name='home'),
       url(r'^browse', 'website.views.browse', name='browse'),
    url(r'^ss', 'website.views.search_places', name='search_places'),
    url(r'^deneme', 'website.views.send_fama', name='send_fama'),
    url(r'^getlistfama', 'website.views.list_fama', name='list_famas'),
    url(r'^famas', 'website.views.famasPage', name='famas'),
    url(r'^fama', 'website.views.thefamaPage', name='fama'),
    url(r'^reporter', 'website.views.ReporterProfilePage', name='profile_page'),
    url(r'^lastfamas/$', 'website.views.LastMinuteFamas', name='last_minute_famas'),
    url(r'^nearfamas/$', 'website.views.FamasOnTheNearPage', name='famas_on_the_near'),
    url(r'^send_ticket/$', 'website.views.SendTicketPage', name='send_ticket'),
    url(r'^send_ticket/done/$', 'website.views.SendTicketDonePage', name='send_ticket_done'),
    url(r'^settings/$', 'website.views.SettingsFama', name='settings_main'),
    url(r'^settings/change_password/$', views.password_change, {'template_name': 'settings/password_change_form.html', 'password_change_form': MyPasswordChangeForm}, name='password_change'),
    url(r'^settings/change_password/done/$', views.password_change_done, {'template_name': 'settings/password_change_done.html'}, name='password_change_done'),
    url(r'^settings/change_email/$', 'website.views.ChangeEmailPage', name='change_email'),
    url(r'^settings/change_email/done/$', 'website.views.ChangeEmailDonePage', name='change_email_done'),
    #url(r'^settings/change_profile_picture/$', 'website.views.ChangeProfilePicturePage', name='change_profile_picture'),
)


#static config
urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT}))

urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))


#auth(user) urls
urlpatterns = urlpatterns + [
    url(r'^login/$', 'website.views.customLogin', {'authentication_form': MyLoginForm}, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', 'website.views.register', name='register'),
    url(r'^password_reset/$', views.password_reset, {'password_reset_form': MyPasswordReset}, name='password_reset'),
    url(r'^password_reset/done/$', views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', views.password_reset_complete, name='password_reset_complete'),
    url(r'^control-register', 'website.views.registerControl', name="registerControl"),
]