from django.conf.urls import patterns, url
from albums import views

#Notes to self $ and ^ are regular expression characters that have special meaning
#The caret means that the pattern must match the start of the string eg rango/hisabout would still load the about page without it
#The dollar means that the pattern must match the end of the string eg rango/aboutblahblah would still load the about page without it 

#The 'r' in front of each regular expression string is optional but recommended.
#It tells Python that a string is "raw" - that nothing in the string should be escaped.


#For the 4th entry in the list 
#the second parameter comes from the parenthesis inserted in urls.py (?P<category_name_slug>[\w\-]+)
#Parenthesis around anything will create new arguments that are passed to views.py

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^new/$', views.new, name='new'),
        url(r'^signup/$', views.register, name='signup'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^test/$', views.test, name='test'),
        url(r'^upload/$', views.upload_photo, name='upload'),
        url(r'^comment/$', views.post_comment, name='comment'),
        url(r'^share/$', views.add_collaborator, name='share'),
        url(r'^(?P<album_name_slug>[\w\-]+)/$', views.memory, name='memory'),
        
       
)
