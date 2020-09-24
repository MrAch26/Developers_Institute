var button = document.getElementById('button');

button.addEventListener('dblclick', function(){

	var newParagraph = document.createElement('p');
	var newText = document.createTextNode('Hello, I am a new text');

	newParagraph.appendChild(newText);

	newParagraph.className = 'text';

	var container = document.getElementsByClassName('container')[0];

	container.appendChild(newParagraph);

});