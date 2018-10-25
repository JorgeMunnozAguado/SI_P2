

$(document).ready(function(){
 $("#medidor").html("This is Hello World by JQuery");
});

function checkForm(){
	var nombre = document.getElementById('')
	var contrasenna = document.getElementById('')
	var repetir = document.getElementById('')
	var email = document.getElementById('')
	var tarjeta = document.getElementById('')
}

function checkUser(){
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function(){
		if(xhttp.readyState == 4 && xhttp.status == 200){
			document.getElementById().innerHTML = xhttp.responseText;
		}
	}
	var dir = "registro.py?nombre=".concat(document.getElementById('nombre').value);
	xhttp.open("GET",dir,true);
	xhttp.send();
}