from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf.urls import handler404
handler404 = 'proj.views.not_found'

import os
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

def basic_url(name, prefix=""):
  return url('^' + prefix + '%s' % name, name, name=name)


## TODO: Move corinthian specific stuff to arcs.corinthian..
urlpatterns += patterns('proj.views',
  basic_url('map'),
  basic_url('login'),
  basic_url('logout'),
  basic_url('signup'),
  basic_url('thankyou'),
  basic_url('stripe_endpoint'),
  url(r'^$', 'splash', name='splash'),
)

urlpatterns += patterns('proj.gather.views',
  basic_url('points'),
  basic_url('states'),
  basic_url('map_data'),
  basic_url('debt_choices'),
  basic_url('debt_total'),
  basic_url('generate_map_json')
)

def corinthian_url(name):
  return basic_url(name, prefix="corinthian/")

urlpatterns += patterns('proj.arcs.corinthian',
  corinthian_url('dtr_generate'),
  corinthian_url('dtr_stats'),
  corinthian_url('dtr_download'),
  corinthian_url('dtr_view'),
  corinthian_url('dtr_wizard'),
  corinthian_url('knowyourstudentdebt'),
  corinthian_url('corinthiansignup'),
  corinthian_url('studentstrike'),
  corinthian_url('corinthiansolidarity')
)

urlpatterns += patterns('proj.arcs.views',
  basic_url('portal')
)


