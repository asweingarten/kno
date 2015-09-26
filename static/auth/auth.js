
// got this from http://www.w3schools.com/js/js_cookies.asp
function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1);
        if (c.indexOf(name) == 0) return c.substring(name.length,c.length);
    }
    return "";
}

function setStatus(status) {
    $('#status').html(status);
}

function authit(token) {
    $.ajax({
	url: "http://kno.ccl.io:7777/v?t=" + token,
    }).done(function(txt){
	console.log("DONE", typeof(txt), txt)
	//setAuthCookie(token)	
    }).fail(function(){
	console.log("FAIL")
    }).always(function(){
	console.log("ALWAYS")
    });
}

var uuid = function(){return"00000000-0000-4000-8000-000000000000".replace(/0/g,function(){return(0|Math.random()*16).toString(16)})}

function setAuthCookie(token) {
    document.cookie = ("token="+token+
		       "; expires=Thu, 31 Dec 2020 12:00:00 UTC; path=/")
}

function createAnonAcct() {
    var uid = uuid();
    console.log("Create " + uid + "?");
     $.ajax({
	url: "http://kno.ccl.io:7777/a?u=" + uid,
    }).done(function(data){
	console.log("DONE", data.result.token, data.result.uid)
	console.log("document.cookie=", document.cookie)
	setAuthCookie(result.token)

    }).fail(function(){
	console.log("FAIL")
    }).always(function(){
	console.log("ALWAYS")
    });   
}

function facebookLogin() {
}

authit("a");
