"""pgbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from users.api.views import UserViewSet
from board.api.views import CommentViewSet, PostViewSet
from stores.api.views import StoreViewSet
from users.api.views import UserViewSet
from items.api.views import ItemListViewSet
from stores.views import AddressFromNaver


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'stores', StoreViewSet)
router.register(r'items', ItemListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/address/', AddressFromNaver.as_view()),
    # path('users/', include("users.urls")),
    path('api-token-auth/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
    path('api-token-verify/', TokenVerifyView.as_view()),
    path(r"api/", include(router.urls))
]
