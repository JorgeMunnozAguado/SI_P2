
setInterval(function(){ conected() }, 3000);

function conected() {
    
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        
        if (this.readyState == 4 && this.status == 200) {
         
            document.getElementById("conected_users").innerHTML = this.responseText;
        }
    };
    
    xhttp.open("POST", "conected_users_ajax", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send();    
}
