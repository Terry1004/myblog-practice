"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', auth_views.login, {'authentication_form': LoginForm}, name = 'login'),
    url(r'^logout/', auth_views.logout_then_login, name = 'logout'),
    url(r'^change-password/$', auth_views.password_change, {'template_name': 'registration/change_password.html'}, name = 'password_change'),
    url(r'^change-password/done$', auth_views.password_change_done, name = 'password_change_done'),
    url(r'^registration/', include('registration.urls', namespace = 'registration')),
    url(r'^account/', include('account.urls', namespace = 'account')),
    url(r'^profiles/', include('profiles.urls', namespace = 'profiles')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
