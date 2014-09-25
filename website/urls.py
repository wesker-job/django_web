from django.conf.urls import patterns, include, url
#from django.contrib import admin
<<<<<<< HEAD
from website.views import hello, current_datetime, hours_ahead, display_meta
from books import views
=======
from website.views import hello, current_datetime, hours_ahead
>>>>>>> 1b3c135edc7def09d57ec00017704174beb30e57
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
<<<<<<< HEAD
=======

>>>>>>> 1b3c135edc7def09d57ec00017704174beb30e57
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^display_meta/$', display_meta),
    url(r'^search_form/$', views.search_form),
    url(r'^search$/$', views.search),
)
