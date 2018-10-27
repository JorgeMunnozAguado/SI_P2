
function setVisible( id ) {

    document.getElementById(id + 'purchase').style.display = 'inline-table';
    document.getElementById(id + 'general').onclick = function(){ setHidden( id ) }
}

function setHidden( id ) {

    document.getElementById(id + 'purchase').style.display = 'none';
    document.getElementById(id + 'general').onclick = function(){ setVisible( id ) }
}