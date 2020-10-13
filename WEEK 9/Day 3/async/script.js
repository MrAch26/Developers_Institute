changeHeadingColor = (color) => {
	document.getElementById('h1').style.backgroundColor = color
}

button = document.getElementById('mybutton');

button.addEventListener('click', ()=>{
	color = document.getElementById('input').value
	
	setTimeout(function(){
		changeHeadingColor(color)
	}, 3000)

	setTimeout(function(){
		changeHeadingColor('pink')
	}, 1000)
});


// function (){}

// () => {}