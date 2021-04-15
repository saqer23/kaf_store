from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'cart'

urlpatterns = [
    path('cart_detail/',views.cart_detail,name="cart_detail"),
    path('add/<int:product_id>',views.cart_add,name="cart_add"),
    path('remove/<int:product_id>',views.cart_remove,name="cart_remove"),

]+static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)