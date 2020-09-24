

var paragraphs = document.getElementsByClassName('text');

paragraphs[0].style.width = '80%';

paragraphs[0].style.height = '200px';

paragraphs[0].style.padding = '0';

paragraphs[0].style.border = '2px solid red';


var button = document.getElementById('button');

button.addEventListener('click', function() {
	
	paragraphs[0].style.width = '100%';

});