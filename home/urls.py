
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chat/', views.chat, name='home'),
    path('blog/<int:blog_id>/', views.blog_post, name='blog_post'),
    path('blogs/', views.blog_result, name='blog_results'),
    path('category/<int:category_id>/', views.category_blogs, name='category_blogs'),
    path('tag/<int:tags_id>/', views.tags_blogs, name='tags_blogs'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
