from django.urls import path
from . import views

app_name = 'educationsections'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:section_id>/', views.section, name='section'),
    path('<int:section_id>/<int:content_id>/', views.detail, name='detail'),
    path('<int:section_id>/get_by_date/', views.date_filter, name='date_filter'),
    path('<int:section_id>/get_by_title/', views.title_filter, name='title_filter'),
    path('<int:section_id>/<author_filter>/', views.author_filter, name='author_filter'),
]