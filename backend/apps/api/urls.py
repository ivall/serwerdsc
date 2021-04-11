from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'servers', views.ServerViewSet, basename='server')
urlpatterns = router.urls