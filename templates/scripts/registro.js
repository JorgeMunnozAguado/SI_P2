

$(document).ready(function(){
 $("#medidor").html("This is Hello World by JQuery");
});

function checkForm(){
	var nombre = document.getElementById('nombre').value.toLowerCase();
	var contrasenna = document.getElementById('password').value;
	var repetir = document.getElementById('repite').value;
	var email = document.getElementById('email').value;
	var tarjeta = document.getElementById('tarjeta').value;
	var fallo=0;
	
	if(contrasenna != repetir){
		fallo=1;
		document.getElementById('').innerHTML=;
		document.getElementById('').style.display='block';
	}
	
	if(tarjeta.length != 12){
		fallo=1;
		document.getElementById('').innerHTML=;
		document.getElementById('').style.display='block';
	}
	
	if(email.includes('@') == false){
		fallo=1;
		document.getElementById('').innerHTML=;
		document.getElementById('').style.display='block';
	}
	
	if(fallo==0){
		document.formulario.submit();
	}
}

function checkUser(){
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
	var contrasenna = document.getElementById('password')
	var repetir = document.getElementById('repite')
	
	if(contrasenna.value == repetir.value){
		document.getElementById("contraIgual").innerHTML = "<p class='bien'>La contrase&ntilde;a es la misma</p>"
		document.getElementById("contraIgual").style.display = 'block';
	}else{
		document.getElementById("contraIgual").innerHTML = "<p class='mal'>La contrase&ntilde;a no es la misma</p>"
		document.getElementById("contraIgual").style.display = 'block';
	}
}