// var x = 1
// var y = 2

// if (y>x) {
//     console.log(y)
// } else {
//     console.log(x)
// }

// ---------EXE2
// var newDog = "Luna"
// console.log(newDog.length+" letters");
// console.log(newDog.toUpperCase());
// console.log(newDog.toLowerCase());

// if (newDog === "Chihuahua"){
//     console.log("I Love Chihuahua")
// } else { 
//     console.log('I prefer the dog of RONNY')
// }

// -------------EXE3

// var x = prompt("How manny cats do yo have ?");
// var num1 = parseInt(x);
// console.log(num1);

// if(num1 % 2 === 0){
//     console.log("I'ts even broooo")
// } else {
//     console.log("i'ts not ahiiiiiii")
// }

// --------------EXE4-------------------

let users = ["IsaacLords666","Abdel54","Lea123", "Princess45", "cat&doglovers", "helooo@000"]

if (users.length===0){
    console.log("No one is online")
} else if(users.length===1){
    console.log(users[0] + " is Online");
} else if (users.length===2) {
    console.log(users[0] + ' & ' + users[1] + " are Online")
} else if (users.length > 2){
    console.log(users[0] + ', ' + users[1] + " and " + (users.length-2)+ " more are Online!")
}

// If there are 2 people, return “<name_user1> and <name_user2> online”.
// If there are n>2 people, return the first two names and add “and n-2 more online”.
// For example, if there are 5 users, return: “user1, user2 and 3 more online”
