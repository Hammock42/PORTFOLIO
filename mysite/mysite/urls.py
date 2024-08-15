from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('coming_soon/', views.coming_soon, name='coming_soon'),
    path('interests/', views.interests, name='interests'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('resume/', views.resume, name='resume'),
    path('skills/', views.skills, name='skills'),
    path('success/', views.success, name='success'),
    path('testimonials/', views.testimonials, name='testimonials'),
]