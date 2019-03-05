from django.conf.urls import url
from . import views


urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
     url('^today/$',views.pics_today,name='picsToday')
    url('^today/$',views.pics_today,name='picsToday'),
    url(r'^search/', views.search_results, name='search_results')
]
