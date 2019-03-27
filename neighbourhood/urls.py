from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from neighbourhood import views

urlpatterns=[
    url(r'^$',views.register,name='article'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^add_business/$',views.add_business,name='add_business'),
    url(r'^home/$',views.home, name='home'),
    url(r'^edit/profile/$',views.edit_profile,name='edit_profile'),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
