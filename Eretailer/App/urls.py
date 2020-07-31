from django.urls import path, re_path

from App import views
urlpatterns = [
    # path('index/', views.index),
    path('home/', views.home, name='home'),

    path('market/', views.market, name='market'),
    re_path('market/typeid=(?P<typeid>\d+)&childid=(?P<childid>\d+)&order=(?P<order>\d+)/', views.market_with_P, name='marketwithP'),

    path('cart/', views.cart, name='cart'),

    path('mine/', views.mine, name='mine'),

    path('register/', views.register, name='register'),
    path('checkuser/', views.check_user, name='checkuser'),

    path('login/', views.login, name='login'),

    path('logout/', views.logout, name='logout'),

    path('addtocart/', views.add_to_cart, name='addtocart'),

    path('subformcart/', views.sub_form_cart, name='subformcart'),

    path('changecartstatus/', views.chenge_cart_status, name='changecartstatus'),

    path('subcart/', views.sub_cart, name='subcart'),

    path('addcart/', views.add_cart, name='addcart'),

    path('allselect/', views.all_select, name='allselect'),

    path('generateorder/', views.generate_order, name='generateorder'),

    path('order/', views.order, name='order'),

    path('ordernotpay/', views.order_not_pay, name='ordernotpay'),

    path('pay/', views.pay, name='pay'),

]
