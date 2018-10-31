function checkPasswordRequisites(password){
	var fallo = 0;
	var capital = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M'];
	var minus = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    var number = ['0','1','2','3','4','5','6','7','8','9'];
    var symbol = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '|', '\\', '[', '{', ']', '}', ':', ';', '\'', '"', ',', '<', '.', '>', '/', '?'];
    var numberCount = 0;
    var minusCount = 0;
    var capitalCount = 0;
    var symbolCount = 0;
    var valido = false;
    var i=0;
    var letra='';
    var height=0;

	if(password.length < 8){
		if(fallo == 0){
			document.getElementById('errorJavascript').innerHTML=document.getElementById('errorJavascript').innerHTML.concat("<br><p>Los requisitos de la contrase&ntilde;a no cumplidos son:</p><li>");
			fallo=1;
		}
		document.getElementById('errorJavascript').innerHTML=document.getElementById('errorJavascript').innerHTML.concat("<ul>Un m&iacute;nimo de 8 caracteres.</ul>");
		height=parseInt(document.getElementById('errorJavascript').style.height);
		height=height+60;
		height_str=height.toString();
		document.getElementById('errorJavascript').style.height=height_str.concat("px");
	}

	for (i = 0; i < password.length; i++) {
        letra = password.charAt(i);
        valido = capital.includes(letra);
        if (valido) {
            capitalCount++;
        }
        valido = number.includes(letra);
        if (valido) {
            numberCount++;
        }
        valido = minus.includes(letra);
        if (valido) {
            minusCount++;
        }
        valido=symbol.includes(letra);
        if (valido) {
            symbolCount++;
        }
    }

    if(capitalCount == 0){
    	if(fallo == 0){
			document.getElementById('errorJavascript').innerHTML=document.getElementById('errorJavascript').innerHTML.concat("<br><p>Los requisitos de la contrase&ntilde;a no cumplidos son:</p><li>");
			fallo=1;
		}
		document.getElementById('errorJavascript').innerHTML=document.getElementById('errorJavascript').innerHTML.concat("<ul>Una letra may&uacute;scula.</ul>");
		height=parseInt(document.getElementById('errorJavascript').style.height);
		height=height+60;
		height_str=height.toString();
		document.getElementById('errorJavascript').style.height=height_str.concat("px");
	}
    if(numberCount == 0){
    	if(fallo == 0){
			document.getElementById('errorJavascript').innerHTML=document.getElementById('errorJavascript').innerHTML.concat("<br><p>Los requisitos de la contrase&ntilde;a no cumplidos son:</p><li>");
			fallo=1;
		}
		document.getElementById('errorJavascript').innerHTML=document.getElementById('errorJavascript').innerHTML.concat("<ul>Un n&uacute;mero.</ul>");
		height=parseInt(document.getElementById('errorJavascript').style.height);
		height=height+60;
		height_str=height.toString();
		document.getElementById('errorJavascript').style.height=height_str.concat("px");
    }
    if(minusCount == 0){
    	if(fallo == 0){
			document.getElementById('errorJavascript').innerHTML=document.getElementById('errorJavascript').innerHTML.concat("<br><p>Los requisitos de la contrase&ntilde;a no cumplidos son:</p><li>");
			fallo=1;
		}
		document.getElementById('errorJavascript').innerHTML=document.getElementById('errorJavascript').innerHTML.concat("<ul>Una letra min&uacute;scula.</ul>");	
		height=parseInt(document.getElementById('errorJavascript').style.height);
		height=height+60;
		height_str=height.toString();
		document.getElementById('errorJavascript').style.height=height_str.concat("px");
    }
    if(symbolCount == 0){
        if(fallo == 0){
			document.getElementById('errorJavascript').innerHTML=document.getElementById('errorJavascript').innerHTML.concat("<br><p>Los requisitos de la contrase&ntilde;a no cumplidos son:</p><li>");
			fallo=1;
		}
		document.getElementById('errorJavascript').innerHTML=document.getElementById('errorJavascript').innerHTML.concat("<ul>Un s&iacute;mbolo.</ul>");	
		height=parseInt(document.getElementById('errorJavascript').style.height);
		height=height+60;
		height_str=height.toString();
		document.getElementById('errorJavascript').style.height=height_str.concat("px");
	}

	if(fallo == 1){
		document.getElementById('errorJavascript').innerHTML=document.getElementById('errorJavascript').innerHTML.concat("</li>");
	}
	
	return fallo;
}

function checkForm(){
	var nombre = document.getElementById('nombre');
	var contrasenna = document.getElementById('password');
	var repetir = document.getElementById('repite');
	var email = document.getElementById('email');
	var tarjeta = document.getElementById('tarjetaValor');
	var fallo=0;
	var height=0;
	var height_str="";

	document.getElementById('errorJavascript').style.height="1px";
	document.getElementById('errorJavascript').innerHTML="";
	if(nombre.value.includes(" ") == true){
		fallo=1;
		document.getElementById('errorJavascript').innerHTML=document.getElementById('errorJavascript').innerHTML.concat("<p>El nombre de usuario no debe contener espacios</p>");
		document.getElementById('errorJavascript').style.display='block';
		height=parseInt(document.getElementById('errorJavascript').style.height);
		height=height+60;
		height_str=height.toString();
		document.getElementById('errorJavascript').style.height=height_str.concat("px");
	}
	if(nombre.value == ''){
		fallo=1;
		document.getElementById('errorJavascript').innerHTML=document.getElementById('errorJavascript').innerHTML.concat("<p>El nombre de usuario no debe estar vacio.</p>");
		document.getElementById('errorJavascript').style.display='block';
		height=parseInt(document.getElementById('errorJavascript').style.height);
		height=height+60;
		height_str=height.toString();
		document.getElementById('errorJavascript').style.height=height_str.concat("px");
	}

	if(fallo == 0){
		fallo = checkPasswordRequisites(contrasenna.value);
		document.getElementById('errorJavascript').style.display='block';
	}else{
		checkPasswordRequisites(contrasenna.value);
	}
	
	if(contrasenna.value != repetir.value){
		fallo=1;
		document.getElementById('errorJavascript').innerHTML=document.getElementById('errorJavascript').innerHTML.concat("<br><p>Las contrase&ntilde;as no son iguales</p>");
		document.getElementById('errorJavascript').style.display='block';
		height=parseInt(document.getElementById('errorJavascript').style.height);
		height=height+60;
		height_str=height.toString();
		document.getElementById('errorJavascript').style.height=height_str.concat("px");
	}
	
	if(tarjeta.value.length != 12){
		fallo=1;
		document.getElementById('errorJavascript').innerHTML=document.getElementById('errorJavascript').innerHTML.concat("<br><p>La tarjeta debe tener 12 caracteres</p>");
		document.getElementById('errorJavascript').style.display='block';
		height=parseInt(document.getElementById('errorJavascript').style.height);
		height=height+60;
		height_str=height.toString();
		document.getElementById('errorJavascript').style.height=height_str.concat("px");
	}
	
	if(email.value.includes('@') == false){
		fallo=1;
		document.getElementById('errorJavascript').innerHTML=document.getElementById('errorJavascript').innerHTML.concat("<br><p>El email debe ser v&aacute;lido</p>");
		document.getElementById('errorJavascript').style.display='block';
		height=parseInt(document.getElementById('errorJavascript').style.height);
		height=height+60;
		height_str=height.toString();
		document.getElementById('errorJavascript').style.height=height_str.concat("px");
	}
	
	if(fallo==0){
		document.getElementById('errorJavascript').style.display='none';
		document.formularioReg.submit();
	}
}

function checkUser(){
	document.getElementById("usuarioRes").style.display = 'none';
	if(document.getElementById('nombre').value.includes(" ") == true){
		document.getElementById("usuarioRes").innerHTML = "<p class='mal'>El nombre de usuario no debe contener espacios.</p>";
		document.getElementById("usuarioRes").style.display = 'block';
		return;
	}
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function(){
		if(xhttp.readyState == 4 && xhttp.status == 200){
			document.getElementById("usuarioRes").innerHTML = xhttp.responseText;
			document.getElementById("usuarioRes").style.display = 'block';
		}
	}
	var dir = "/server.wsgi/compr_usuario/".concat(document.getElementById('nombre').value.toLowerCase());
	xhttp.open("GET",dir,true);
	xhttp.send();
}


function checkPassword(){
    var contrasenna = document.getElementById('password');
    var repetir = document.getElementById('repite');

    
    if(repetir.value == "" || contrasenna.value == ""){
        document.getElementById("contraIgual").style.display = 'none';
    }else if(contrasenna.value != null && repetir.value != null && contrasenna.value != repetir.value){
        document.getElementById("contraIgual").innerHTML = "<p class='mal'>La contrase&ntilde;a no es la misma</p>";
        document.getElementById("contraIgual").style.display = 'block';
    }else if(repetir.value != null && contrasenna.value != null && contrasenna.value == repetir.value){
        document.getElementById("contraIgual").innerHTML = "<p class='bien'>La contrase&ntilde;a es la misma</p>";
        document.getElementById("contraIgual").style.display = 'block';
    }
}
