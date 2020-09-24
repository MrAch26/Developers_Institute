



var paragraph = document.getElementsByClassName('text'),
 small = document.getElementById('small'),
 medium = document.getElementById('medium'),
 big = document.getElementById('big'),
 uppercase = document.getElementById('uppercase'),
 lowercase = document.getElementById('lowercase');


	small.addEventListener('click', function(e) {
	
	for(var i = 0; i < paragraph.length; i++){

		paragraph[i].style.fontSize = '10px';

	}
	

});

medium.addEventListener('click', function(e) {
	
	for(var i = 0; i < paragraph.length; i++){

		paragraph[i].style.fontSize = '16px';

	}
	

});

big.addEventListener('click', function(e) {
	
	for(var i = 0; i < paragraph.length; i++){

		paragraph[i].style.fontSize = '20px';

	}
	

});

uppercase.addEventListener('click', function(e) {
	
	for(var i = 0; i < paragraph.length; i++){

		paragraph[i].style.textTransform = 'uppercase';

	}
	

});

lowercase.addEventListener('click', function(e) {
	
	for(var i = 0; i < paragraph.length; i++){

		paragraph[i].style.textTransform = 'lowercase';

	}
	

});