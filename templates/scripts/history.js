
function setVisible( id ) {

    purchase = document.getElementById(id + 'purchase');
    purchase.style.visibility = 'visible';
    purchase.style.position = 'static';
    document.getElementById(id + 'general').onclick = function(){ setHidden( id ) }
}

function setHidden( id ) {

    purchase = document.getElementById(id + 'purchase');
    purchase.style.visibility = 'hidden';
    purchase.style.position = 'absolute';
    document.getElementById(id + 'general').onclick = function(){ setVisible( id ) }
}