from django.conf.urls import patterns, include, url
from website.views import hello, current_datetime, hours_ahead, display_meta
from books.views import search, search_form#views
from contact.views import contact, thanks
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^display_meta/$', display_meta),
    url(r'search_form/$', search_form), #url(r'^search_form/$', views.search_form),
    url(r'search/$', search), #url(r'^search/$', views.search),
    url(r'^contact/$', contact),
    url(r'^contact/thanks/$',thanks),
    #url(r'^contact/thanks/$', views.contact),
)
