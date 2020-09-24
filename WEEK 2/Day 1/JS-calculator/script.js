// alert('WELCOME TO MY CALCULATOR')

// var x = prompt("Enter a Value", "placeholder");
// var y = prompt("Add something to that Value", "0");

// var num1 = parseInt(x);
// var num2 = parseInt(y);

// var result = parseInt(num1+num2)
// console.log(result);

// alert('The adddition of both number is '+ (result));

// console.log("in case you don't remember --> "+ (result))


// -------------------------------- Add-Sub-Mul-Div

var x = prompt('What do you want to do ? Add, Sub, Mul, Div ?')

var y = prompt("Enter a Value", "placeholder");
var z = prompt("Add something to that Value", "0");
var num1 = parseInt(y);
var num2 = parseInt(z);
var result = parseInt(num1+num2);
var result1 = parseInt(num1-num2);
var result2 = parseInt(num1*num2);
var result3 = parseInt(num1/num2);

if (x === 'Add' || x === '+') {
        alert(' The Addition is = ' + (result))
    } else if (x === 'Sub' || x === '-'){
        alert(' The Substraction is = ' + result1)
    } else if (x === 'Mul' || x === '*'){
        alert(' The Multiplication is = ' + result2)
    } else if (x === 'Div' || x === '/'){
        alert(' The Division is = ' + result3)
    }

// if (x === 'Add' || x === '+') {
//     var num1 = parseInt(prompt('Enter Number'));
//     var num2 = parseInt(prompt('Enter Number'));
//     var result = (num1+num2)

//     alert(' The Addition is =' + (result))
//     } else if (x === 'Sub' || x === '-'){
//         var num1 = parseInt(prompt('Enter Number'));
//         var num2 = parseInt(prompt('Enter Number'));
//         var result = (num1-num2)
    
//         alert(' The Substraction is =' + result)
//     } else if (x === 'Mul' || x === '*'){
//         var num1 = parseInt(prompt('Enter Number'));
//         var num2 = parseInt(prompt('Enter Number'));
//         var result = (num1*num2)
    
//         alert(' The Multiplication is =' + result)
//     } else if (x === 'Div' || x === '/'){
//         var num1 = parseInt(prompt('Enter Number'));
//         var num2 = parseInt(prompt('Enter Number'));
//         var result = (num1/num2)
    
//         alert(' The Division is =' + result)
//     }
    

