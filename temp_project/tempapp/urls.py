from django.conf.urls import url
from tempapp import views


# template tagging
app_name ='tempapp'

urlpatterns = [
    url('registrer/', views.register, name = 'register'),
    #url('relative/', views.relative, name = 'relative'),
    url('base/', views.base, name = 'base'),
    url('index/', views.index, name = 'index'),
    url('user_login/', views.user_login, name = 'user_login'),
    url('user_logout/', views.user_logout, name = 'user_logout'),
]
