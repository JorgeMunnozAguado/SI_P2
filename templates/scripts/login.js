

function check() {
            
    var boolean = true;
    
    var name = document.getElementById('name');
    var password = document.getElementById('password');
    
    var log = document.getElementById('log');
    
    log.innerHTML = "";
    log.style.visibility = "hidden";
    
    if (!checkText("Introduzca un nombre válido.", name, log)) boolean = false;
    if (!checkText("Introduzca una contraseña válida.", password, log)) boolean = false;
   
    if (boolean && document.getElementById('keepSession').checked) {

        var json = '{"name":"' + name.value +'","password":"' + password.value + '"}';

        setCookie("keepSession", json, "432000");
    }

    return boolean;
}


function setLogin() {

    var text = getCookie("keepSession");
    
    if (text == "") return;

    var json = JSON.parse(text);

    document.getElementById('name').value = json.name;
    document.getElementById('password').value = json.password;
    document.getElementById('keepSession').checked = true;
}
