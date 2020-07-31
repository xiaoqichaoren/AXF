$(function () {
    // 验证用户名是否存在
    $("#username").change(function () {
        var username = $("#username").val();
        $.getJSON("/App/checkuser/", {"username": username}, function (data) {
            // console.log(data);
            if (data["status"] == 1200) {
                $("#username_info").html("√").css("color", "green");
            } else if (data["status"] == 1400) {
                $("#username_info").html("用户已存在").css("color", "red");
            }
        })
    })
    // 验证邮箱格式
    $("#email").change(function () {
        var email = $(this).val();
        var re = /^(\w)+(\.\w+)*@(\w)+((\.\w+)+)$/;
        if (re.test(email)) {
            $("#email_info").html('√').css("color", "green");
        } else {
            $("#email_info").html('请输入正确邮箱地址').css("color", "red");
        }
    })
    // 验证密码长度是否过短
    $("#password").change(function () {
        var password = $(this).val();
        if (password.length < 6) {
            $("#password_info").html("密码必须多于6位数").css("color", "red");
        } else {
            $("#password_info").html("√").css("color", "green");
        }
    })
    // 验证两次密码是否相同
    $("#password_confirm").change(function () {
        var password = $("#password").val();
        var password_confirm = $(this).val();
        if ($("#password_info").css("color") == "rgb(0, 128, 0)") {
            if (password == password_confirm) {
                $("#password_confirm_info").html("√").css("color", "green");
            } else {
                $("#password_confirm_info").html("两次输入不一致").css("color", "red");
            }
        }
    })

})


function submit_check() {

    var username_color = $("#username_info").css("color");
    var email_color = $("#email_info").css("color");
    var password_color = $("#password_info").css("color");
    var password_confirm_color = $("#password_confirm_info").css("color");
    var PASS_COLOR = "rgb(0, 128, 0)";

    //md5加密
    var password = $("#password").val();
    $("#password").val(hex_md5(password));

    return (username_color == PASS_COLOR) &&
        (email_color == PASS_COLOR) &&
        (password_color == PASS_COLOR) &&
        (password_confirm_color == PASS_COLOR)
}
