from django.conf import settings
from django.contrib import admin
from blog import views as blog_views
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.home, name='home'),
    path('about/', blog_views.about, name='about'),
    path('contact/', blog_views.contact, name='contact'),
    path('blogs/', blog_views.blogs, name='blogs'),
    path('category/<str:category>/', blog_views.category, name='category'),
    path('blogs/<slug:article_slug>/', blog_views.blog_details, name='article_detail'),
    re_path(r'^robots\.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    re_path(r'^ads\.txt$', TemplateView.as_view(template_name="Ads.txt", content_type="text/plain")),
    path('', include('app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
