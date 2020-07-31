$(function () {

    $("#all_types").click(function () {
        $("#all_types_container").show();
        $("#all_type_logo").removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");
        $("#sort_container").hide();
        $("#sort_rule_logo").addClass("glyphicon-chevron-down").removeClass("glyphicon-chevron-up");
    })


    $("#all_types_container").click(function () {
        $(this).hide();
        $("#all_type_logo").addClass("glyphicon-chevron-down").removeClass("glyphicon-chevron-up");

    })


    $("#sort_rule").click(function () {
        $("#sort_container").show();
        $("#sort_rule_logo").addClass("glyphicon-chevron-up").removeClass("glyphicon-chevron-down");
        $("#all_types_container").hide();
        $("#all_type_logo").removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");
    })

    $("#sort_container").click(function () {
        $(this).hide();
        $("#sort_rule_logo").addClass("glyphicon-chevron-down").removeClass("glyphicon-chevron-up");
    })


//    添加商品到购物车
    $(".addShopping").click(function () {
        // 拿到商品id发送给服务器
        var $addgood = $(this);
        var goodid = $addgood.attr("goodid");

        $.getJSON("/App/addtocart/", {"goodid": goodid}, function (data) {
            console.log(data);
            if (data["status"] == 1300) {
                window.alert("请先登录");
                window.open("/App/login/", target = "_self");
            } else if (data["status"] == 1200) {
                $addgood.prev("span").html(data["good_num"]);
            }
        })

    })
    // 减少商品
    $(".subShopping").click(function () {
        //    拿到商品id发送给服务器
        var $subgood = $(this);
        var goodid = $subgood.attr("goodid");

        $.getJSON("/App/subformcart/", {"goodid": goodid}, function (data) {
            console.log(data);
            if (data["status"] == 1300) {
                window.alert("请先登录");
                window.open("/App/login/", target = "_self");
            } else if (data["status"] == 1200) {
                $subgood.next("span").html(data["good_num"]);
            } else if (data["status"] == 1404) {
                window.alert("不能再减啦！");
            }
        })
    })


})