from django.urls import re_path as url
from basic_app import views

#TEMPLATE URLS!
app_name = 'basic_app'

urlpatterns=[
    url(r'^register/$',views.register,name='register')
]
