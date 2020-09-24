// // Exercise 1 GOLD:)
// let word = prompt("Enter a word");
// let word2 = word;
// word = word.replace(/[aeiouAEIOU]/gi, "");
// console.log(word);
// // BONUS WOHOOO
// word2 = word2.replace(/[aeiouAEIOU]/gi, "t");
// console.log(word2);

// EXE 2
// var language = prompt("Choose a Language : FR-EN-HB ? ");

// switch (language) {
//   case 'FR','fr':
//     console.log("Bonjour");
//     break;

//   case 'EN', 'en':
//         console.log("Hello");
//         break;

//   case 'HB', 'hb':
//     console.log("Shalom");
//     break;

//   default:
//     console.log("Go back to your country");
//     break;

// }

// EXE 3
// var x = prompt('what was your grade bro ?');
// var grade = parseInt(x);

// if (grade >= 90){
//     console.log('A, Bravo')
// } else if (grade >=80){
//     console.log("B")
// } else if (grade >=70){
//     console.log("C")
// } else if (grade<70){
//     console.log("D, you're not going out this WE BAD BOYYYY !")
// } else {
//     console.log("Whut ?")
// }

// EXE4

// let zip = 65454;
// let zipPrompt = prompt("Write your code here");
// pattern = /^\d{5}$/;
// console.log(pattern.test(zipPrompt));

// ^^^^^ USING REGEX ^^^^^

// var zip = prompt("what is your zipcode ?");
// var n = zip.length;

// //|| zip.indexOf(" ")!== -1 --- for space

// if (n !== 5 || isNaN(zip) ){
//     console.log("ERROR")
// } else {
//     console.log("Very Good")
// }

// if (zip >= 10000 && zip <=99999){
//     console.log("good")
// } else {
//     console.log("error")
// }

// if (zip >= 1 && zip<=99999){
//     var validZip = zip.slice(0,5)
//     console.log(validZip)
// } else {
//     console.log("Please type in a valid ZipCode Coño !")
// }

// if (n===5 && isNaN(x)===false && ){
//    console.log("Great, thanks");
// } else {
//     console.log("error")
// }

// ------------------------------------

// XP-NINJA - exe 1

// var x = prompt("give your birthdate (YYYY) ??")//kid
// var y = prompt("Birthdate of your mom (YYYY) ?")//mother
// var birthdate1 = parseInt(x);
// var birthdate2 = parseInt(y);

// alert("The year ..... is "+((birthdate1-birthdate2)+birthdate1));

// XP_NINJA - exe2

// var str = prompt("Whats your word ?");
// var n = str.length;

// if (n >= 3) {
//   if (str.endsWith("ing")) {
//     str = str + "ly";
//   } else {
//     str = str + "ing";
//   }
// }
// alert(str);
