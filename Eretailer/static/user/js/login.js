function login_check() {
    //md5加密
    var password = $("#password").val();
    $("#password").val(hex_md5(password));

    return true;
}