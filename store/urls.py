from django.urls import path
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('customers', views.CustomerViewSet)

carts = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts.register('items', views.CartItemViewSet, basename='carts-items')

products = routers.NestedDefaultRouter(router, 'products', lookup='product')
products.register('reviews', views.ReviewViewSet, basename='products-reviews')

urlpatterns = router.urls + products.urls + carts.urls
