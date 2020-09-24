// XP-exe1 

// function ordinal_suffix_of(i) {
//     var j = i % 10,
//         k = i % 100;
//     if (j == 1 && k != 11) {
//         return i + "st";
//     }
//     if (j == 2 && k != 12) {
//         return i + "nd";
//     }
//     if (j == 3 && k != 13) {
//         return i + "rd";
//     }
//     return i + "th";
// }

// var colors = ["Yellow","Red","Orange","Gold","Yellow","Red","Orange","Gold"]

// for (let i=0 ; i<colors.length ; i++){
//     // i = 1 - i;
//     console.log("my "+ ordinal_suffix_of(i+1) +" favorite color is "+colors[i]);
// }


// EXE2
// let x = ["YITJAKKKKKK","Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
// let names = x.sort();
// console.log(names);
// var finalName ="";

// for (i=0 ; i<names.length ; i++){
//     finalName = finalName+names[i].charAt(0); 
// }

// console.log(finalName);
// console.log(names[i].charAt(0)+" Society")

// // EXE3

// var x = prompt("Put a number please, merci");
// x = parseInt(x)

// while (x<=10) {
//    x = prompt("PUT again you lost hahaha")
// } 

// EXE4

// let people = ["Greg", "Mary", "Devon", "James"];

// for (i=0;i<people.length;i++){//1
//     console.log(people[i])
// }

// people.shift()//2

// for (i=0;i<people.length;i++){
//     console.log(people[i])
// }

// people.splice(people.indexOf("James"),1,"Jason");//3
// people.splice(2,1,"Jason");//3

// for (i=0;i<people.length;i++){
//     console.log(people[i])
// }

// people.push("Daniel");//4

// for (i=0;i<people.length;i++){
//     console.log(people[i])
// }



// for (i=0;i<people.length;i++){ //5
//     if (people[i]==="Mary") { break; }
//     console.log(people[i])
// } 


// people = people.slice(1,3)//6--
// console.log(people)

// var place = people.indexOf("Mary");//7--
// console.log(place);

// var place2 = people.indexOf("Foo");//8--
// console.log(place2);


// var last = (people[people.length-1])//9
// console.log(last)

// var last = people[3]; ===


// EXE5


// let age = [20,5,12,43,98,55];


// var sum = 0; // 1
// for (i=0;i<age.length;i++){
//     sum=sum+age[i]
// }
// console.log(sum)

// for (isaac of age){ // 2
//     if (isaac%2===0){
//         console.log(isaac)
//     } else {
//         continue;
//     }
// }

// var largestNumber = 0;

// for (isaac of age){ // 3
//     if (isaac>largestNumber){
//         largestNumber=isaac;
//     } 
// }

// console.log(largestNumber);



// XP_GOLD !

// EXE1

// const GUEST_LIST = {
//     Randy: "Germany",
//     Karla: "France",
//     Wendy: "Japan",
//     Norman: "England",
//     Sam: "Argentina",
//     Isaac: "Venezuela",
//     Daniel: "Belgium"
//   }

//   console.log(Object.keys(GUEST_LIST));
//   console.log(Object.values(GUEST_LIST));

// var x = prompt("What's your name");


// if (x in GUEST_LIST){
//     console.log("Hi I am "+x+" and I'm from "+GUEST_LIST[x])
// } else {
//     console.log("I AM A GUEST :( ")
// }


// EXE2

// var family = {
    
//     name:"Simpson",
//     favoriteFood:"Bagel",
//     city:"Netanya",
//     numberOfMembers:5
// }

// // console.log(Object.keys(family));
// // console.log(Object.values(family));

// for (property in family){
//     console.log(property)
// } 

// for (values in family){
//     console.log(family[values])
// } 

// // EXE3

// let building = {
//     number_levels : 4,
//     number_of_apt_by_level : {
//         "1": 3,
//         "2": 4,
//         "3": 9,
//         "4": 2,
//     },
//     name_of_tenants : ["Sarah", "Dan", "David"],
//     number_of_rooms_and_rent:  {
//         "Sarah": [3, 2000],
//         "Dan":  [4, 1000],
//         "David": [1, 10],
//     },
// }

// console.log(building.number_levels);

// console.log(building.number_of_apt_by_level[1]+" \
// "+building.number_of_apt_by_level[3]);

// console.log(Object.values(building)[1][3]+" \
// "+Object.values(building)[1][1]);

// console.log(building.name_of_tenants[1]+' \
// '+building.number_of_rooms_and_rent.Dan[0]);

// var rentDavid = building.number_of_rooms_and_rent.David[1];
// var rentSarah = building.number_of_rooms_and_rent.Sarah[1];
// var rentDan = building.number_of_rooms_and_rent.Dan[1];

// while (rentSarah + rentDavid > rentDan) {
// rentDan = prompt("What is your new rent offer ?")  
// console.log("The new rent of Dan is "+ rentDan);
// }

// // EXE4

// var person1 = {
//     fullName:"Usain Bolt",
//     mass:90,
//     height:190
// }
// var person2 = {
//     fullName:"Cristiano Ronaldo",
//     mass:47,
//     height:200
// }


// // weight/height*height = BMI


// console.log(person1.mass);
// var bmi1 = (Math.round(person1.mass/(person1.height*person1.height)*10000*10)/10)
// var bmi2 = (Math.round(person2.mass/Math.pow(person2.height,2)*10000*10)/10)
// console.log(bmi1)
// // (Math.pow(person1.height,2))

// if(bmi1<bmi2){
//     console.log("Usain Bolt is in shpae !")
// } else {
//     console.log("Cristiano is a spaghetti 😂")
// }

// // EXE1 - XP NINJA 

// let x = prompt("Type in a number...")
// var array = x.split("");
// console.log(array)

// var total = 0

// for (i=0;i<array.length;i++){
// total += parseInt(array[i]);
// }

// if (total %3===0) {
//     alert('TRUE !')
// } else {
//     alert("It's Isaac's fault ! ")
// }
// console.log(total)

// EXE2

// var name1 = prompt("What's your name?");
// // var courseName =  prompt("What's the course ?");
// // var grade1 = prompt("What grade will you have ? think about loser...")
// // var coef = prompt("What's the coef of this course ?");

// let average = {
// name:name1
// // course:courseName,
// // grade:grade1,
// // coefficient:coef
// }
// console.log(average.name)
// while (isEmpty(average.name)) {
//     name1 = prompt("What's your name?");
//     // courseName =  prompt("What's the course ?");
//     // grade1 = prompt("What grade will you have ? think about loser...")
//     // coef = prompt("What's the coef of this course ?");
// } 


   //Global Object
   var average = {};
   var name;
   var namecourse;
   var grade;
   var coefficient;
   var process;
   function ask() {
       name = prompt('What is your name?');
       while (name === null || name === '') {
           name = prompt('What is your name?');
       }
       namecourse = prompt('Tell me the name of the course (Ex: Maths, Physics, etc…)');
       while (namecourse === null || namecourse === '') {
           namecourse = prompt('Incorrect Answer, Tell me the name of the course (Ex: Maths, Physics, etc…)');
       }
       grade = prompt('Tell me the grade you think you are going to have in ' + namecourse);
       while (grade === null || grade === '' || isNaN(grade)) {
           grade = prompt('Incorrect Answer, Tell me the grade you think you are going to heve in ' + namecourse);
       }
       coefficient = prompt('Tell me the coeffiecient of ' + namecourse);
       while (coefficient === null || coefficient === '' || isNaN(coefficient)) {
           coefficient = prompt('Incorrect Answer, Tell me the coeffiecient of ' + namecourse);
       }
       var course = {
           name: namecourse,
           grade: grade,
           coefficient: coefficient
       }
       average["Course"] = course;
       process = prompt('Do you want to continue the process with a new course, grade, and coefficient? (Yes or No)');
       while (process === null || process === '') {
           process = prompt('Do you want to continue the process with a new course, grade, and coefficient? (Yes or No)');
       }
       if (process === 'Yes' || process === 'yes') {
           //call function again
           ask();
       } else if (process === 'No' || process === 'no') {
           console.log('Average Object:', average);
           console.log(name + ' Your semester Average in ' + namecourse + ' is ' + (grade * coefficient) / 5);
       } else {
           console.log('Please try again');
           ask();
       }
   }
   //call function first time
   ask();


