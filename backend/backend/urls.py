from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from accounts import views as accounts_views

from cafes import views as cafe_views

router = routers.DefaultRouter()
router.register(r'users', accounts_views.UserViewSet)
router.register("tags", cafe_views.TagViewSet)
router.register("cafes", cafe_views.CafeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("admin", admin.site.urls)
]