from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.

# def index(request):
#     return render(request, 'index.html')
from django.urls import reverse

from App.funs import sum_cart_price
from App.models import HomeWheel, HomeNav, HomeMustBuy, HomeShop, HomeShow, FoodType, Goods, User, Cart, Order, \
    Order_Goods
from App.utils import ALL_TYPE, TOTAL, PRICE_UP, PRICE_DOWN, SALE_UP, SALE_DOWN, STATUS_OK, STATUS_EXIST, DEFAULT_ICON, \
    STATUS_DONT_LOGIN, STATUS_DONT_EXIST, STATUS_FAIL, ORDER_NOT_PAY, ORDER_NOT_ACCEPT, ORDER_NOT_ASSESS, ORDER_PAY, \
    ORDER_ACCEPT
from Eretailer.settings import MEDIA_KEY_PREFIX, STATIC_URL


def home(request):
    home_wheels = HomeWheel.objects.all()

    home_navs = HomeNav.objects.all()

    home_mustbuys = HomeMustBuy.objects.all()

    home_shops = HomeShop.objects.all()
    home_shop0_1 = home_shops[0:1]
    home_shop1_3 = home_shops[1:3]
    home_shop3_7 = home_shops[3:7]
    home_shop7_11 = home_shops[7:11]

    home_shows = HomeShow.objects.all()

    data = {
        'title': '首页',
        'home_wheels': home_wheels,
        'home_navs': home_navs,
        'home_mustbuys': home_mustbuys,
        'home_shop0_1': home_shop0_1,
        'home_shop1_3': home_shop1_3,
        'home_shop3_7': home_shop3_7,
        'home_shop7_11': home_shop7_11,
        'home_shows': home_shows,
    }

    return render(request, 'main/home.html', context=data)


def market(request):
    default = FoodType.objects.get(typesort=1)
    param = {
        'typeid': default.typeid,
        'childid': 0,
        'order': 0,
    }
    return redirect(reverse('App:marketwithP', kwargs=param))
def market_with_P(request, typeid, childid, order):
    food_types = FoodType.objects.all()

    goods = Goods.objects.filter(categoryid=typeid)

    # 判断子分类
    if childid == ALL_TYPE:
        pass
    else:
        goods = goods.filter(childcid=childid)

    # 判断排序规则
    if order == TOTAL:
        pass
    elif order == PRICE_UP:
        goods = goods.order_by('price')
    elif order == PRICE_DOWN:
        goods = goods.order_by('-price')
    elif order == SALE_UP:
        goods = goods.order_by('productnum')
    elif order == SALE_DOWN:
        goods = goods.order_by('-productnum')

    # 全部分类:0#进口水果:103534#国产水果:103533 -> [['全部分类', '0'],['进口西瓜', '103534'],['国产水果', '103533']]
    food_type_childnames = food_types.get(typeid=typeid).childtypenames
    food_type_childnames_list = [list(reversed(i.split(':'))) for i in food_type_childnames.split('#')]
    type_menu_name = dict(food_type_childnames_list)[childid]

    # 排序规则列表
    order_list = [
        [TOTAL, '综合排序'],
        [PRICE_UP, '价格升序'],
        [PRICE_DOWN, '价格降序'],
        [SALE_UP, '销量升序'],
        [SALE_DOWN, '销量降序'],
    ]
    sort_menu_name = dict(order_list)[order]

    data = {
        'title': '闪购',
        'food_types': food_types,
        'goods': goods,
        'this_typeid': int(typeid),
        'food_type_childnames_list': food_type_childnames_list,
        'this_childid': childid,
        'type_menu_name': type_menu_name,
        'order_list': order_list,
        'this_order': order,
        'sort_menu_name': sort_menu_name,
    }

    return render(request, 'main/market.html', context=data)


def cart(request):
    if request.is_login:
        carts = Cart.objects.filter(user=request.user)

        is_all_select = not Cart.objects.filter(is_select=False).exists() and carts.exists()

        data = {
            'title': '购物车',
            'carts': carts,
            'is_all_select': is_all_select,
            'total_price': sum_cart_price(request.user),
        }

        return render(request, 'main/cart.html', context=data)
    else:
        return redirect(reverse('App:login'))


def mine(request):
    user_id = request.session.get('user_id')
    data = {
        'title': '我的',
        'is_login': False,
    }

    if user_id:
        user = User.objects.get(pk=user_id)
        data['is_login'] = True
        data['username'] = user.username
        if not user.icon:
            data['icon'] = STATIC_URL + DEFAULT_ICON
        else:
            data['icon'] = MEDIA_KEY_PREFIX + user.icon.url
        data['order_not_pay'] = Order.objects.filter(user=user).filter(status=ORDER_NOT_PAY).count()
        data['order_not_accept'] = Order.objects.filter(user=user).filter(status__in=[ORDER_PAY, ORDER_NOT_ACCEPT]).count()
        data['order_not_assess'] = Order.objects.filter(user=user).filter(status__in=[ORDER_ACCEPT, ORDER_NOT_ASSESS]).count()


    return render(request, 'main/mine.html', context=data)


def register(request):
    if request.method == 'GET':
        data = {
            'title': '注册',
        }
        return render(request, 'user/register.html', context=data)
    elif request.method == 'POST':
        username = request.POST.get('username')

        email = request.POST.get('email')

        password = request.POST.get('password')
        password = make_password(password)

        icon = request.FILES.get('icon')

        user = User()
        user.username = username
        user.email = email
        user.password = password
        user.icon = icon

        user.save()

        return redirect(reverse('App:login'))
# ajax注册异步校验
def check_user(request):
    username = request.GET.get('username')
    json = {
        'status': STATUS_OK,
        'msg': 'username can be used',
    }
    if User.objects.filter(username=username).exists():
        json['status'] = STATUS_EXIST
        json['msg'] = 'user already exist'
        return JsonResponse(data=json)
    else:
        return JsonResponse(data=json)


def login(request):
    if request.method == 'GET':
        data = {
            'title': '登录',
        }
        return render(request, 'user/login.html', context=data)
    elif request.method == 'POST':
        username = request.POST.get('username')

        password = request.POST.get('password')

        users = User.objects.filter(username=username)
        if users.exists():
            user = users[0]
            if check_password(password, user.password):

                request.session['user_id'] = user.id

                return redirect(reverse('App:home'))
            else:
                return redirect(reverse('App:login'))
        else:
            return redirect(reverse('App:register'))


def logout(request):
    request.session.flush()
    return redirect(reverse('App:mine'))


def add_to_cart(request):
    goodid = request.GET.get('goodid')
    json = {
        'status': STATUS_OK,
    }

    if request.is_login:  # 是否已经登陆
        carts = Cart.objects.filter(user=request.user).filter(goods_id=goodid)
        if carts.exists():
            cart = carts[0]
            cart.goods_num = cart.goods_num + 1

        else:
            cart = Cart()
            cart.goods_id = goodid
            cart.user = request.user

        cart.save()
        json['good_num'] = cart.goods_num

    else:   # 匿名用户对象（就是没登陆）
        json['status'] = STATUS_DONT_LOGIN

    return JsonResponse(data=json)


def sub_form_cart(request):
    goodid = request.GET.get('goodid')
    json = {
        'status': STATUS_OK,
    }
    if request.is_login:
        carts = Cart.objects.filter(user=request.user).filter(goods_id=goodid)
        if carts.exists():
            cart = carts[0]
            cart.goods_num = cart.goods_num - 1
            if cart.goods_num == 0:
                cart.delete()
                json['good_num'] = 0
            else:
                cart.save()
                json['good_num'] = cart.goods_num
        else:
            json['status'] = STATUS_DONT_EXIST

    else:  # 匿名用户对象（就是没登陆）
        json['status'] = STATUS_DONT_LOGIN

    return JsonResponse(data=json)


def chenge_cart_status(request):
    cart_id = request.GET.get('cart_id')
    cart = Cart.objects.get(pk=cart_id)

    json = {
        'status': STATUS_OK,
    }

    if cart.user == request.user:
        cart.is_select = not cart.is_select
        cart.save()
        json['is_select'] = cart.is_select
        json['is_all_select'] = not Cart.objects.filter(user=request.user).filter(is_select=False).exists()
        json['total_price'] = sum_cart_price(request.user)
    else:
        json['status'] = STATUS_FAIL

    return JsonResponse(data=json)


def sub_cart(request):
    cart_id = request.GET.get('cart_id')
    cart = Cart.objects.get(pk=cart_id)

    json = {
        'status': STATUS_OK,
    }

    if cart.user == request.user:
        cart.goods_num = cart.goods_num - 1
        if cart.goods_num == 0:
            cart.delete()
            json['status'] = STATUS_DONT_EXIST
        else:
            cart.save()
            json['good_num'] = cart.goods_num
        json['total_price'] = sum_cart_price(request.user)
    else:
        json['status'] = STATUS_FAIL

    return JsonResponse(data=json)


def add_cart(request):
    cart_id = request.GET.get('cart_id')
    cart = Cart.objects.get(pk=cart_id)

    json = {
        'status': STATUS_OK,
    }

    if cart.user == request.user:
        cart.goods_num = cart.goods_num + 1
        cart.save()
        json['good_num'] = cart.goods_num
        json['total_price'] = sum_cart_price(request.user)
    else:
        json['status'] = STATUS_FAIL

    return JsonResponse(data=json)


def all_select(request):
    cart_list_str = request.GET.get('cartliststr')
    cart_id_list = cart_list_str.split('|')

    carts = Cart.objects.filter(id__in=cart_id_list)

    json = {
        'status': STATUS_OK,
        'is_all_select': True,
    }

    if len(carts.filter(user=request.user)) == len(carts):
        if carts[0].is_select:
            json['is_all_select'] = False

        for cart in carts:
            cart.is_select = not cart.is_select
            cart.save()
        json['total_price'] = sum_cart_price(request.user)
    else:
        json['status'] = STATUS_FAIL

    return JsonResponse(data=json)


def generate_order(request):
    carts = Cart.objects.filter(user=request.user).filter(is_select=True)

    order = Order()
    order.user = request.user
    order.total = sum_cart_price(request.user)
    order.save()

    for cart in carts:
        order_goods = Order_Goods()
        order_goods.order = order
        order_goods.num = cart.goods_num
        order_goods.goods = cart.goods
        order_goods.save()

        cart.delete()


    json = {
        'status': STATUS_OK,
        'order_id': order.id,
    }

    return JsonResponse(data=json)


def order(request):
    order_id = request.GET.get('orderid')
    order = Order.objects.get(pk=order_id)
    data = {
        'title': '订单详情',
        'order': order,
    }
    return render(request, 'order/order.html', context=data)


def order_not_pay(request):
    if request.is_login:
        orders = Order.objects.filter(user=request.user).filter(status=ORDER_NOT_PAY)
        data = {
            'title': '订单列表',
            'orders': orders,
        }
    else:
        return redirect(reverse('App:login'))
    return render(request, 'order/order_not_pay.html', context=data)


def pay(request):
    order_id = request.GET.get('order_id')
    order = Order.objects.get(pk=order_id)
    order.status = ORDER_PAY
    order.save()

    json = {
        'status': STATUS_OK,
    }
    return JsonResponse(data=json)
