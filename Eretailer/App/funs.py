from App.models import Cart


def sum_cart_price(user):
    carts = Cart.objects.filter(user=user).filter(is_select=True)
    total = 0
    for cart in carts:
        total += cart.goods_num * cart.goods.price
    return format(total, '.2f')
