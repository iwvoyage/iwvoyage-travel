from django.urls import path
from .views import post_list_view, post_detail_view, posts_by_category, posts_by_tag

app_name = 'post'

urlpatterns = [
    path('', post_list_view, name='post_list'),
    path('category/<slug:slug>/', posts_by_category, name='posts_by_category'),
    path('tag/<slug:slug>/', posts_by_tag, name='posts_by_tag'),
    path('<slug:slug>/', post_detail_view, name='post_detail'),
]
