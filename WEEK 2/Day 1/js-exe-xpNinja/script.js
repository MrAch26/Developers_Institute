// 5 >= 1
// 0 === 1
// 4 <= 1
// 1 != 1
// "A" > "B"
// "B" < "C"
// "a" > "A"
// "b" < "A"
// true === false
// true != true

// console.log() ---> for everything

// // ------------- exe-2

// let c; // undefined

// let a = 34;
// let b = 21
// a=2 // so a=2 and != 34

// (a+b) // 23
// c // still undefined

// console.log(3 + 4 + '5'); // 75
// // 3+4 = 7 --> + '5' = 75 

// // --------------- exe-3

// var list = prompt('two numbers commas : ')
// var list1 = list.split(",")
// console.log(list1);


// alert('the addition is ' + (list1[0]*list1[1]))


// ----------- EXE-4

var n = parseInt(prompt("Enter a number of 'O' you want"));

if (n === 1|| n === 2){
    alert("boom");
} else if ((n%2===0) && (n%5===0)) {
    var x ="B"+("o".repeat(n))+"m "+"!";
    alert(x.toUpperCase());
} else if (n%2===0){
    var x ="B"+("o".repeat(n))+"m "+"!";
    alert(x);
} else if (n%5===0){
    var x = "B"+("o".repeat(n))+"m ";
    alert(x.toUpperCase());
} else if (n>2){
    var x ="B"+("o".repeat(n))+"m ";
    alert(x);
} else {
    alert("Start Over MANIAK !");
}



// Examples
// 4 ➞ "Boooom!"
// // There are 4 "o"s and 4 is divisible by 2 (exclamation mark included)
// 1 ➞ "boom"
// // 1 is lower than 2, so we return "boom"


