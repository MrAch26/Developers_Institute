var x = prompt("Type 5 different words separated by commas 😎");
var phrase= x.split(",");


console.log("************");

for (i=0;i<phrase.length;i++) {
    phrase[i]="*   "+phrase[i]+" "
    console.log(phrase[i])
}


console.log("************");

// phrase.unshift("*********");
// phrase.push("*********");
// Hello,My,Friend,Is,Hahaha

// ----------------

// function frame(){
//     //let userWords = prompt("Please imput at least three words, each separated with \",\" !");
//     let userWords = prompt("Please imput at least three words!");
//     let arrayWords = userWords.split(" ");
//     let border = "*".repeat(userWords.length)
//     console.log(border);
//     for(let word of arrayWords){
//         console.log("*" + " " + word + " ".repeat(userWords.length - word.length - 3) + "*");
//     }
//     console.log(border);
// }
// frame();