from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from accounts import views as accounts_views
from cafes import views as cafe_views

router = routers.DefaultRouter()
router.register(r"users", accounts_views.UserViewSet)
router.register("tags", cafe_views.TagViewSet)
router.register("cafes", cafe_views.CafeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("admin", admin.site.urls),
    path(
        "api/token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "api/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"
    ),
]
