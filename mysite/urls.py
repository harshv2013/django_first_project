from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views, login, logout
from django.urls import path

urlpatterns = [
    url('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # url('accounts/login/$', views.login(), name='login'),
    # url('accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url('', include('blog.urls')),
]