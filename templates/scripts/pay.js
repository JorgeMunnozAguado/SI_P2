
function addBalance() {
    
    var xhttp = new XMLHttpRequest();
    
    var balance = document.getElementById("balance");
    var log = document.getElementById("log");
    
    xhttp.onreadystatechange = function() {
        
        if (this.readyState == 4 && this.status == 200) {
         
            if (this.responseText == "OK") {
                
                log.classList.add("okey");
                log.style.display = "block";
                document.getElementById("log_p").innerHTML = "Saldo actualizado";
                
            } else if (this.responseText == "ERROR") {
                
                log.classList.remove('okey');
                document.getElementById("log_p").innerHTML = "Saldo incorrecto";
            }
        }
    };
    
    xhttp.open("POST", "/server.wsgi/balance_ajax", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send('balance=' + balance.value);    
}
