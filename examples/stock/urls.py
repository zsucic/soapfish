from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',    
     url(r'^stock/soap11$', "stock.web.views.dispatch11"),
     url(r'^stock/soap12$', "stock.web.views.dispatch12"),
)
