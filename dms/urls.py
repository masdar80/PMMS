from django import views
from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),
    path('logout/', logout, name='logout'),
    path('', index, name='index'),
    path('image_upload', image_upload, name='image_upload'),
    #path('image_upload', MailCreatView.as_view(), name='image_upload'),

    path('success', success, name='success'),
    path('success_edit', success_edit, name='success_edit'),
    path('about/', about, name='about'),
    path('table/', table, name='table'),
    #path('logout/', logout, name='logout'),
    path('view_img/<int:mail_id>/', view_img, name='view_img'),
    path('del/<pk>/',  MailsDeleteView.as_view(), name='del'),
    path('detail/<int:mail_id>/', detail, name='detail'),
    path('delete/<int:mail_id>/', mail_delete, name='mail_delete'),
    path('remove/<int:mail_id>/', mail_remove, name='mail_remove'),
    path('edit/<int:mail_id>/', mail_edit, name='mail_edit'),
    path('readocr/<int:mail_id>/', readOCR, name='readocr'),
    path('media/images/<str:img_url>/', view_img_form, name='view_img_form'),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
