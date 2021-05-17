from rest_framework.routers import DefaultRouter
from .views import CompanyView,FeatureView,CarView,SpecificationView
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views


router = DefaultRouter()
router.register('company', CompanyView, basename='company')
router.register('feature', FeatureView, basename='feature')
router.register('car', CarView,basename='car')
router.register('spec', SpecificationView,basename='spec')



urlpatterns = [
    path('api/',include(router.urls)),  
    path('api/token',jwt_views.TokenObtainPairView.as_view(), name='token_object_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
]