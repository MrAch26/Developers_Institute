let str1 = 'mix';
let str2 = 'pod';

let newWord = str2.slice(0, 2) + str1.slice(2) + " " + str1.slice(0, 2) + str2.slice(2);
console.log(newWord);