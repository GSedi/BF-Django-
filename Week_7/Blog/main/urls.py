from django.urls import path, re_path
from main import views


urlpatterns = [
     path('', views.index, name='index'),
     path('show_posts/', views.show_posts, name='show_posts'),
     path('add_post/', views.add_post, name='add_post'),
     path('<int:id>/update_post/', views.update_post, name='update_post'),
     path('<int:id>/delete_post/', views.delete_post, name='delete_post'),
     path('<int:id>/post_details/', views.post_details, name='post_details'),
     path('add_comment/', views.add_comment, name='add_comment'),
     path('<int:id>/update_comment/', views.update_comment, name='update_comment'),
     path('<int:id>/delete_comment/', views.delete_comment, name='delete_comment'),
]
