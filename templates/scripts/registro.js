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
	if(contrasenna.value != repetir.value){
		fallo=1;
		document.getElementById('errorJavascript').innerHTML=document.getElementById('errorJavascript').innerHTML.concat("<p>Las contrase&ntilde;as no son iguales</p>");
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
	/*if(tarjeta.value. == true){
		fallo=1;
		document.getElementById('errorJavascript').innerHTML=document.getElementById('errorJavascript').innerHTML.concat("<br><p>La tarjeta debe tener solo numeros</p>");
		document.getElementById('errorJavascript').style.display='block';
		height=parseInt(document.getElementById('errorJavascript').style.height);
		height=height+60;
		height_str=height.toString();
		document.getElementById('errorJavascript').style.height=height_str.concat("px");
	}*/
	
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
	var dir = "/compr_usuario/".concat(document.getElementById('nombre').value.toLowerCase());
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
