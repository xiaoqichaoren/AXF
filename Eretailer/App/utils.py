ALL_TYPE = '0'

# ORDER
TOTAL = '0'
PRICE_UP = '1'
PRICE_DOWN = '2'
SALE_UP = '3'
SALE_DOWN = '4'

# STATUS_CODE
STATUS_OK = 1200
STATUS_FAIL = 1444
STATUS_EXIST = 1400
STATUS_DONT_EXIST = 1404
STATUS_DONT_LOGIN = 1300

# 默认头像地址：在static/icon/下
DEFAULT_ICON = 'icon/default.jpg'

# 中间件校验地址
CHECK_PATH = [
    '/App/addtocart/',
    '/App/subformcart/',
    '/App/cart/',
    '/App/changecartstatus/',
    '/App/subcart/',
    '/App/addcart/',
    '/App/allselect/',
    '/App/generateorder/',
    '/App/order/',
    '/App/ordernotpay/',
    '/App/pay/',
]

# 订单状态
# 既有流程
ORDER_NOT_PAY = 1   # 未付款
ORDER_PAY = 2   # 已付款
ORDER_NOT_ACCEPT = 3   # 未收货
ORDER_ACCEPT = 4   # 已收货
ORDER_NOT_ASSESS = 5   # 未评价
ORDER_ASSESS = 6   # 已评价
# 待选流程
ORDER_AFTERMARKET = 7   # 售后中
ORDER_RETURN = 8   # 已退货
ORDER_CHANGING = 9   # 换货中
ORDER_CHANGED = 10   # 已换货

