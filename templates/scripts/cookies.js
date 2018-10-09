

function addToBasket(id, name, href) {
    
    var i;
    var text = getCookie("basket");
        
    var json_ret = '{"films":[';
   
    if (text != "") {

        var json = JSON.parse(text);

        for (i = 0; i < json.films.length; i++) {
        
            json_ret += JSON.stringify(json.films[i]) + ",";
        }
    }
	
    json_ret += '{"name":"' + name +'","href":"' + href + '"}]}';
    
    setCookie("basket", json_ret, "30");
    
    id.classList.add('basket-get');
    id.childNodes[0].src = 'images/carrito-less.png';
}


/* Function getCookie from WCS <https://www.w3schools.com/js/js_cookies.asp> */
function getCookie(cname) {
    
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

/* Function setCookie from WCS <https://www.w3schools.com/js/js_cookies.asp> */
function setCookie(cname, cvalue, exminutes) {
    
    var d = new Date();
    
    d.setTime(d.getTime() + (exminutes * 60 * 1000));
    var expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}
