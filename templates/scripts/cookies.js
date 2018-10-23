

function addToBasket(id, name) {
    
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        
        if (this.readyState == 4 && this.status == 200) {
         
            id.classList.add('basket-get');
            id.onclick = function(){ removeFromBasket(this, name, false) }
            id.childNodes[0].src = 'images/carrito-less.png';
        }
    };
    
    xhttp.open("POST", "ajax_url", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send('type=add&name=' + name);    
}

function removeFromBasket(id, name, aux) {

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        
        if (this.readyState == 4 && this.status == 200) {
         
            if (aux == false) {
        
                id.classList.remove('basket-get');
                id.onclick = function(){ addToBasket(this, name) }
                id.childNodes[0].src = 'images/carrito-plus.png';
                
            } else if (aux == true) {
                
                elem = document.getElementById(id);

                	c = elem.childNodes;

                	for (i = 0; i < c.length; i++) {
                    c[i].parentNode.removeChild(c[i])
                	}

                	elem.parentNode.removeChild(elem);
            }
        }
    };
    
    xhttp.open("POST", "ajax_url", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send('type=remove&name=' + name);  
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
