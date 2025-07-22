"""
URL configuration for tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from quickstart import views
router = routers.DefaultRouter()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    
    # # Authentication endpoints
    # path('api/login/', views.LoginView.as_view(), name='login'),
    # path('api/logout/', views.LogoutView.as_view(), name='logout'),
    
    # # Authentication examples
    # path('api/token-auth-example/', views.TokenAuthExampleView.as_view(), name='token-auth-example'),
    # path('api/session-auth-example/', views.SessionAuthExampleView.as_view(), name='session-auth-example'),
    # path('api/basic-auth-example/', views.BasicAuthExampleView.as_view(), name='basic-auth-example'),
    # path('api/multiple-auth-example/', views.MultipleAuthExampleView.as_view(), name='multiple-auth-example'),
    # path('api/public/', views.PublicView.as_view(), name='public'),
    
    # # Demo endpoints
    # path('api/data-demo/', views.DataDemoView.as_view(), name='data-demo'),
    # path('api/request-demo/', views.requestDemoView.as_view(), name='request-demo'),
    # path('api/auth-demo/', views.authDemoView.as_view(), name='auth-demo'),
    
    # Django REST Framework browsable API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/UserList/', views.UserList.as_view(), name='UserList'),
    path('api/GroupList/', views.GroupList.as_view(), name='GroupList'),
    path('api/addUser/', views.AddUser.as_view(), name='addUser'),
    path('api/userdetail/<int:pk>/', views.userdetail.as_view(), name='userdetail'),
    path('api/userdetail/<str:username>/', views.userdetail.as_view(), name='userdetailusername'),
    path('api/destroy/<int:pk>/', views.destroy.as_view(), name='destroy'),
    path('api/UpdateUser/<str:username>/', views.UpdateUserView.as_view(), name='UpdateUser'),
    path('api/DeleteUser/<int:pk>/', views.DeleteUserView.as_view(), name='DeleteUser'),
    path('api/user/<str:username>/', views.RetrieveUpdateDestroyUser.as_view(), name='user-detail'),
    path('api/RetrieveUserView/', views.RetrieveUserView.as_view(), name='RetrieveUserView')
]
