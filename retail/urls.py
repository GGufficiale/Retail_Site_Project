from django.urls import path
from django.views.decorators.cache import cache_page

from retail.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ContactPageView, InfoPageView, HomeView
from retail.apps import RetailConfig

app_name = RetailConfig.name
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    # метод для отображения отдельной страницы с товаром (по одному товару)
    path('retail/contact/', ContactPageView.as_view(), name='contact'),
    path('retail/info/', InfoPageView.as_view(), name='info'),
    # В декоратор кеширования cache_page передается время его жизни (60 сек) и ссылка на контроллер (contact).
    # Это позволяет кешировать весь контроллер
    path('retail/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('retail/list/', ProductListView.as_view(), name='product_list'),
    path('retail/create/', ProductCreateView.as_view(), name='product_create'),
    path('retail/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('retail/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_confirm_delete'),
]
