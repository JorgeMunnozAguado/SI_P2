

function check() {
            
    var boolean = true;
    
    var name = document.getElementById('name');
    var password = document.getElementById('password');
    
    var log = document.getElementById('log');
    
    log.innerHTML = "";
    log.style.visibility = "hidden";
    
    if (!checkText("Introduzca un nombre válido.", name, log)) boolean = false;
    if (!checkText("Introduzca una contraseña válida.", password, log)) boolean = false;
    
    return boolean;
}
