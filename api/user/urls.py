from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import CustomUserViewSet, signin, signout


router = routers.DefaultRouter()
router.register(r'', CustomUserViewSet)

urlpatterns = [
    path('login/', signin, name='signin'),
    path('logout/<str:uuid>/', signout, name='signout'),
    path('gettoken/', TokenObtainPairView.as_view()),
    path('refreshtoken/', TokenRefreshView.as_view()),
    path('verifytoken/', TokenVerifyView.as_view()),
    path('', include(router.urls)),
]
