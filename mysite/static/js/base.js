// codigo js - base - input palavras
function mudaEstado( par ) {
    if (document.getElementById( par ).name == par ) {
        document.getElementById( par ).style.color = "white"
    	document.getElementById( par ).name = "";
    } else {
        document.getElementById( par ).style.color = "black"
        document.getElementById( par ).name = par;
    }
}