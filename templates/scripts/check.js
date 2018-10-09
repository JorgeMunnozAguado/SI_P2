
function checkText(string, text, log) {
    
    replaceSpace(text);
    
    if (text.value.length < 1) return setFalse(string, text, log);
        
    else return setTrue(text);
}

function checkEmail(string, email, log) {
    
    replaceSpace(email);
    
    if (!email.value.includes("@")) return setFalse(string, email, log);
        
    else return setTrue(email);
}

function checkUnsignedInt(string, number, log) {
    
    replaceSpace(number);
    
    var num = number.value;
    
    if (parseInt(num) <= 0 || isNaN(num) || num.includes(".") || num.length <= 0) return setFalse(string, number, log);
        
    else return setTrue(number);
}


/* ###################### FUNCIONES AUXILIARES ######################*/

function replaceSpace(input) {
    
    input.value = input.value.replace(/\s/g, "");
}

function setFalse(string, input, log) {
    
    log.innerHTML += string + "<br>";
    log.style.visibility = "visible";
    
    input.classList.add('error');
    
    return false;
}

function setTrue(input) {
    
    input.classList.remove('error');
    
    return true;
}
