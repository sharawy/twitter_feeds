from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # Examples:
    #url route for home view
    url(r'^$', 'feed.views.home', name='home'),
    #url rout for ajax request
    url(r'^get_feed/', 'feed.views.getfeed',name='getfeed'),

    url(r'^admin/', include(admin.site.urls)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #identify where static files is (css/js)
