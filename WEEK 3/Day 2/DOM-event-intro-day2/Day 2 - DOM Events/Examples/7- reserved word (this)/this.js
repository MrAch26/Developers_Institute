

var paragraph = document.getElementsByClassName('text');

for(var i = 0; i < paragraph.length; i++){

	paragraph[i].addEventListener('click', function () {
		this.className = 'text red-backgroud';   //reserved word refering to a specific item in object or array
	});

}

//Example

// var plant = {

// 	color: 'green',

// 	size: 'big',

// 	information: function(){
// 		console.log('The color of the plant is ' + this.color);
// 	}

// }


// plant.information();

// https://developer.mozilla.org/es/docs/Web/JavaScript/Referencia/Operadores/this