function hangingGame() {
  alert("WELCOME TO THE HANGING GAME MADE BY DANIEL HIHI");
  alert("To Play this game you will have to Open your console (option+cmd+j)");

  var firstPlayer = prompt("Player 1, ENTER a word (min 8 characters)😋");
  // var player1 = firstPlayer.split('');
  // console.log(player1);
  firstPlayer = firstPlayer.toLowerCase();

  while (firstPlayer.length < 8) {
    var firstPlayer = prompt("Player 1, ENTER a word 😋");
  }

  var wordStars = [];
  var try10 = 5;
  var findTrue = false;
  var wrongLetters = [];
  var remainingLife = firstPlayer.length;

  for (i = 0; i < firstPlayer.length; i++) {
    wordStars[i] = "*";
  }
  console.log(wordStars);

  while (remainingLife > 0) {
    var letterGuess = prompt("Try to guess, Give ONE letter !");
    findTrue == false;
    if (try10 < 1) {
      console.log("You LOST !!!");
      alert("GameOver");
      break;
    } else if (letterGuess == null) {
      break;
    } else if (letterGuess.length !== 1) {
      alert("Just give ONE letter !");
    } else if (
      wrongLetters.includes(letterGuess) == true ||
      wordStars.includes(letterGuess) == true
    ) {
      console.log(
        "You have already chosen this letter " + "You have " + try10 + " Lives"
      );
      findTrue == false;
    } else if (
      firstPlayer.includes(letterGuess) == false &&
      wordStars.includes(letterGuess) == false
    ) {
      try10 = try10 - 1;
      findTrue == false;
      wrongLetters.push(letterGuess);
      console.log("WRONG ! you have " + try10 + " lives left");
      console.log("Those are the letters you already typed :" + wrongLetters);
    } else {
      for (j = 0; j < firstPlayer.length; j++) {
        if (firstPlayer[j] === letterGuess) {
          wordStars[j] = letterGuess;
          remainingLife--;
          findTrue = true;
          console.log(wordStars.join(" "));
        }
      }
      if (findTrue == false) {
        try10--;
      }
    }
  }

  if (remainingLife == 0) {
    findTrue = false;
    console.log("YOU GOT IT! YOU WON! refresh to play again 🤩");
  }
}

// hangingGame();

// while (firstPlayer.length<8) {
//     firstPlayer = prompt("Player 1, ENTER a word 😋");
//     var player1 = firstPlayer.split('');
// for (i=0;i<player1.length;i++){
//     player1[i]="*"
// }
// }
// console.log(player1);
