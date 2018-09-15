$("#submitBtn").click(function (event) {
    log(clientip); //logs IP
    $.cookie("client_ip_cookie", clientip, { path: '/', expires : 10});
})