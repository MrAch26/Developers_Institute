// SCOPE
// Scope refers to the visibility of variables. In other words, 
// which parts of your program can see or use it. Normally, 
// every variable has a global scope. 
// Once defined, every part of your program can access a variable.



// Global Variable - Declared outside of a function
var message = 'Hello, I am a variable';

function greet (){
	alert(message);
}

// greet();


// Local Variable - Declared inside a function

function sayGooobye(){

	var sayGooobye = 'Bye, see you later';

	alert(sayGooobye);

}

sayGooobye();






//-----------------------------------------------------------

/*
A variable can be accessed from the inside out

This allows us to protect our code, so that it is not modified from outside
*/

//-----------------------------------------------------------


// (   function(){


// 	 All Javascript code



// }()   )
