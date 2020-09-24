

var paragraphs = document.getElementsByClassName('text'),
 red = document.getElementById('red'),
 blue = document.getElementById('blue'),
 green = document.getElementById('green'),
 bgblack = document.getElementById('bgblack'),
 bgyellow = document.getElementById('bgyellow');


	red.addEventListener('click', function(e) {
	
	for (var i = 0; i < paragraphs.length; i++) {
		paragraphs[i].style.color = 'red';
	}

});

blue.addEventListener('click', function(e) {
	
	for (var i = 0; i < paragraphs.length; i++) {
		paragraphs[i].style.color = 'blue';
	}

});

green.addEventListener('click', function(e) {
	
	for (var i = 0; i < paragraphs.length; i++) {
		paragraphs[i].style.color = 'green';
	}

});

bgblack.addEventListener('click', function(e) {
	
	for (var i = 0; i < paragraphs.length; i++) {
		paragraphs[i].style.background = 'black';
	}

});

bgyellow.addEventListener('click', function(e) {
	
	for (var i = 0; i < paragraphs.length; i++) {
		paragraphs[i].style.background = 'yellow';
	}

});