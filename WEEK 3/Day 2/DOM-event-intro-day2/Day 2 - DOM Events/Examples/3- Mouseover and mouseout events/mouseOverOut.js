var paragraph = document.getElementsByClassName('text')[0];

// mouseover event

paragraph.addEventListener('mouseover', function() {
	
var newParagraph = document.createElement('p');

var newText = document.createTextNode('Hello, I am a new text');

newParagraph.appendChild(newText);

newParagraph.setAttribute('class','text');

newParagraph.id = 'addedParagraph';

var container = document.getElementsByClassName('container')[0];

container.appendChild(newParagraph);

});



// mouseout event

paragraph.addEventListener('mouseout', function() {
	
	var addedParagraph = document.getElementById('addedParagraph');
	var container = document.getElementsByClassName('container')[0];

	container.removeChild(addedParagraph);

});