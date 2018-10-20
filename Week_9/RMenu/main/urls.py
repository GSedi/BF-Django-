from django.urls import path
from main import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('show_restaurants/', views.show_restaurants, name='show_restaurants'),
    # path('add_restaurant/', views.add_restaurant, name='add_restaurant'),
    # path('<int:id>/update_restaurant/', views.update_restaurant, name='update_restaurant'),
    # path('<int:id>/delete_restaurant/', views.delete_restaurant, name='delete_restaurant'),
    path('', views.IndexView.as_view(), name='index'),
    path('restaurants/', views.RestaurantList.as_view(), name='show_restaurants'),
    path('restaurant/create/', views.RestaurantCreateView.as_view(), name='create_restaurant'),
    path('restaurant/detail/<int:pk>/', views.RestaurantDetailView.as_view(), name='detail_restaurant'),
    path('restaurant/update/<int:pk>/', views.RestaurantUpdateView.as_view(), name='update_restaurant'),
    path('restaurants/delete/<int:pk>/', views.RestaurantDeleteView.as_view(), name='delete_restaurant'),
]