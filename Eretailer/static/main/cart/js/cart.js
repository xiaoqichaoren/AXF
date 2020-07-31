// 页面加载准备好了     就是页面基本结构加载完成
$(function () {


    $(".confirm").click(function () {
        var current_li = $(this);
        var cart_id = current_li.parents("li").attr("cartid");
        console.log(cart_id);

        $.getJSON("/App/changecartstatus/", {"cart_id": cart_id}, function (data) {
            console.log(data);
            if (data["status"] == 1200) {
                if (data["is_select"]) {
                    current_li.find("span").find("span").html("√");
                    if (data["is_all_select"]) {
                        $(".all_select span span").html("√");
                    }
                } else {
                    current_li.find("span").find("span").html("");
                    $(".all_select span span").html("");
                }
                $("#total_price").html(data["total_price"]);
            }
        })
    })


    $(".subShopping").click(function () {
        // 代表记住我们这一样  真实是点击的button
        var current_li = $(this);
        var cart_id = current_li.parents("li").attr("cartid");
        console.log(cart_id);

        $.getJSON("/App/subcart/", {"cart_id": cart_id}, function (data) {

            console.log(data);

            if (data["status"] == 1200) {
                current_li.next().html(data["good_num"]);
            } else if (data["status"] == 1404) {
                current_li.parents("li").remove();
            }
            $("#total_price").html(data["total_price"]);
        })

    })


    $(".addShopping").click(function () {

        var current_li = $(this);
        var cart_id = current_li.parents("li").attr("cartid");
        console.log(cart_id);

        $.getJSON("/App/addcart/", {"cart_id": cart_id}, function (data) {
            console.log(data);

            if (data["status"] == 1200) {
                current_li.prev().html(data["good_num"]);
            }
            $("#total_price").html(data["total_price"]);
        })

    })

    //全选
    $(".all_select").click(function () {

        //    如果有未选中的，应该执行操作是全部选中
        //    并且让自己的按钮变成选中状态
        //    如果全都是选中的，全部取消选中
        var $all_select = $(this);
        var select_id = [];
        var unselect_id = [];

        $(".confirm").each(function () {
            var $confirm = $(this);

            var cartid = $confirm.parents("li").attr("cartid");

            if ($confirm.find("span").find("span").html().trim()) {
                select_id.push(cartid);
            } else {
                unselect_id.push(cartid);
            }
        })

        console.log(select_id, unselect_id);
        var cartlist = [];
        if (unselect_id.length > 0) {
            cartlist = unselect_id;
        } else {
            cartlist = select_id;
        }
        $.getJSON("/App/allselect/", {"cartliststr": cartlist.join("|")}, function (data) {
            console.log(data);
            if (data["status"] == 1200) {
                if (data["is_all_select"]) {
                    $(".confirm span span").html("√");
                    $all_select.find("span").find("span").html("√");
                } else {
                    $(".confirm span span").html("");
                    $all_select.find("span").find("span").html("");
                }
            }
            $("#total_price").html(data["total_price"]);
        })
    })


    //生成订单
    $("#generate_order").click(function () {

        var select_id = [];
        var unselect_id = [];

        $(".confirm").each(function () {
            var $confirm = $(this);

            var cartid = $confirm.parents("li").attr("cartid");

            if ($confirm.find("span").find("span").html().trim()) {
                select_id.push(cartid);
            } else {
                unselect_id.push(cartid);
            }
        })

        if (select_id.length == 0){
            return
        }
        $.getJSON("/App/generateorder/", function (data) {
            console.log(data);
            if (data["status"] == 1200) {
                window.open("/App/order/?orderid=" + data["order_id"], target="_self");
            }
        })
    })


})