window.addEventListener('load', function() { //Solves the problem for executing first the js
	
	function chooseColor(){

	var triggerStatus = document.getElementById('favoriteColor').checked;

	if (triggerStatus == true) {

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

var inputColorFavorite = document.getElementById('favoriteColor');

inputColorFavorite.addEventListener('change', chooseColor);

});