from django.conf.urls import url

from tea.views import *

urlpatterns = [
    url(r'^$', ProductsList.as_view(), name='products_list'),
    url(r'^page/(?P<page>\d+)/$', ProductsList.as_view(), name='products_list'),
    url(r'^add_product/$', ProductCreate.as_view(), name='add_product'),
    url(r'^product/(?P<id>\d+)/$', ProductDetail.as_view(), name='product_detail'),
    url(r'^product/(?P<id>\d+)/delete/$', ProductDelete.as_view(), name='product_delete'),
    url(r'^product/(?P<id>\d+)/update/$', ProductUpdate.as_view(), name='product_update'),
    url(r'^product/(?P<id>\d+)/add_to_cart/$', AddToCart.as_view(), name='add_to_cart'),
    url(r'^register/$', RegisterFormView.as_view()),
    url(r'^login/$', LoginFormView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^add_buyer/$', BuyerCreate.as_view(), name='add_buyer'),
    url(r'^cart/update/$', UpdateCart.as_view()),
    url(r'^cart/delete/(?P<id>\d+)/$', DeleteFromCart.as_view()),
    url(r'^cart/clear/$', ClearCart.as_view()),
    url(r'^cart/$', CartView.as_view(), name='cart'),
    url(r'^order/$', OrderView.as_view(), name='order'),
    url(r'^view/$', view=view_tr)
]