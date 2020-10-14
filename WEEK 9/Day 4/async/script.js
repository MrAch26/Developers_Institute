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


function print_to_screen(r){
	console.log(r)
}

console.log("HERE 1")

fetch(
	"https://api.chucknorris.io/jokes/random"
)
.then(response => response.json())
.then(data => console.log(data['value']))
.catch(error => console.log("error"))


console.log("HERE 2")