// addEventListener(); 

var button = document.getElementById('button');
var button2 = document.getElementById('button2');

function alertUser(){

	alert('Hello World');

}

button.addEventListener('click', alertUser);

// removeEventListener(); 

function removerAlert(){

	button.removeEventListener('click', alertUser);

}

button2.addEventListener('click', removerAlert);


// https://developer.mozilla.org/en-US/docs/Web/Events