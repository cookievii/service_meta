from rest_framework.routers import DefaultRouter

from api.views import MetaViewSet

router = DefaultRouter()
router.register("meta", MetaViewSet, basename="meta")
