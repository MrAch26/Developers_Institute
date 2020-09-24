

function chooseColor(){

	var triggerState = document.getElementById('favoriteColor').checked;

	if (triggerState == true) {

		var radios = document.getElementById('radios');
		radios.classList.remove("disabled");

		document.getElementById('green').disabled = false;
		document.getElementById('blue').disabled = false;
		document.getElementById('other').disabled = false;

	} else{

		var radios = document.getElementById('radios');
		radios.classList.add("disabled");

		document.getElementById('green').disabled = true;
		document.getElementById('blue').disabled = true;
		document.getElementById('other').disabled = true;
	}

}


// Change event

var inputFavoriteColor = document.getElementById('favoriteColor');

inputFavoriteColor.addEventListener('change', chooseColor);