

function addToBasket(id, name, aux) {
    
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        
        if (this.readyState == 4 && this.status == 200) {
         
            
            if (aux == "full") {
              
                document.getElementById("desc-basket").innerHTML = "Eliminar del carrito";
                id.onclick = function(){ removeFromBasket(this, name, "full") }
                document.getElementById("imagen-basket").src = '/images/carrito-less.png';
                
            } else {
                
                id.classList.add('basket-get');
                id.onclick = function(){ removeFromBasket(this, name, false) }
                id.childNodes[0].src = '/images/carrito-less.png';
            }
        }
    };
    
    xhttp.open("POST", "/ajax_url", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send('type=add&name=' + name);    
}

function removeFromBasket(id, name, aux) {

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        
        if (this.readyState == 4 && this.status == 200) {
         
            if (aux == "full") {
            
                document.getElementById("desc-basket").innerHTML = "Añadir al carrito";
                id.onclick = function(){ addToBasket(this, name, "full") }
                document.getElementById("imagen-basket").src = '/images/carrito-plus.png';
                
            } else if (aux == false) {
        
                id.classList.remove('basket-get');
                id.onclick = function(){ addToBasket(this, name, "") }
                id.childNodes[0].src = '/images/carrito-plus.png';
                
            } else if (aux == true) {
                
                var elem = document.getElementById(id);
                
                var price = document.getElementById("real-price");
                price.innerHTML = (parseInt(price.innerText) - parseInt(elem.getElementsByClassName("price")[0].innerText)) + " €";

                	c = elem.childNodes;

                	for (i = 0; i < c.length; i++) {
                    c[i].parentNode.removeChild(c[i])
                	}

                	elem.parentNode.removeChild(elem);
            }
        }
    };
    
    xhttp.open("POST", "/ajax_url", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send('type=remove&name=' + name);  
}

function changeNumber(id, name) {
    
    var xhttp = new XMLHttpRequest();
    
    number = document.getElementById(id + "input").value;
    var elem = document.getElementById(id + "price");
    
    var price_one = parseInt(elem.innerText) / parseInt(number);
    
    if (parseInt(number) == 0) removeFromBasket(id + 'film', name, true)
    
    if (parseInt(number) < 0 || isNaN(number) || number.includes(".") || number.length <= 0) {
        
        document.getElementById(id + "input").style.border = "1px solid red";
        return;
    }
    
    document.getElementById(id + "input").style.border = "1px solid #AFAFAF";
    
    xhttp.onreadystatechange = function() {
        
        if (this.readyState == 4 && this.status == 200) {
            
            var price = document.getElementById("real-price");
            var newprice = (parseInt(elem.innerText) / parseInt(this.responseText)) * parseInt(number);
            price.innerHTML = (parseInt(price.innerText) - parseInt(elem.innerText) + newprice) + " €";
            elem.innerHTML = newprice + ' €';
        }
    };
    
    xhttp.open("POST", "/ajax_url", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send('type=number&name=' + name + '&number=' + number);    
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
