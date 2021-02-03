from django.urls import path, include
from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.BlogHome, name='blog'),
    path('<int:blog_id>/', views.article, name='article')
]
