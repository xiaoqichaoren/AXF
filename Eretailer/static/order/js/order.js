$(function () {

    $("#pay").click(function () {
        var orderid = $(this).attr("orderid");
        $.getJSON("/App/pay/", {"order_id": orderid}, function (data) {
            if (data["status"] == 1200) {
                window.open("/App/mine/", target="_self");
            }
        })
    })

    $("#cancel").click(function () {
        window.open("/App/cart/", target="_self");
    })

})