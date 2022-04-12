from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'todos', TodoListViewSet, basename='todos')
urlpatterns = router.urls
