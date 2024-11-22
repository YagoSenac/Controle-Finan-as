from rest_framework.routers import DefaultRouter
from .views import CategoryViewset, TransactionViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewset, basename='category')
router.register(r'transactions', TransactionViewSet, basename='transaction')

urlpatterns = router.urls