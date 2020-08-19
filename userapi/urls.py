from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.userapiOverview,name="overview"),
    path('users/', views.users,name="users"),
    path('user-create/', views.userCreate, name="user-create"),
    path('user-detail/<str:pk>/', views.userDetail, name="user-detail"),
	path('user-update/<str:pk>/', views.userUpdate, name="user-update"),
	path('user-patch/<str:pk>',views.patch, name="patch"),
    path('user-delete/<str:pk>/', views.userDelete, name="user-delete"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]