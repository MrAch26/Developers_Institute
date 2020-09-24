var notBad = ("The food was not bad");
var array = notBad.split(" ");
console.log(array)
var not = array.indexOf("not");
var bad = array.indexOf("bad")

if (not < bad) {
    console.log("the dinner is good");
} else {
    console.log(notBad);
}

// var findNot = notBad.substring(13,16)
// var findBad = notBad.substr(17,4)

// console.log(findNot)
// console.log(findBad)


// if (findBad > findNot) {
//     console.log("THE food is very TAIM miam :)")
// } else {
//     console.log(notBad)
// }

