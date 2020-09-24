function beerSong() {  
    var bottles;
    var bottlesLeft;

    for (i = prompt("How many bottles of beer do you have ?"); i >= 1; i--) {
      if (i == 1) {
        bottles = "bottle";
        bottlesLeft = "No bottles of beer on the wall!";
      } else {

        bottles = "bottles";
        bottlesLeft = i - 1 + " bottles of beer on the wall!";

      } 
      console.log(i+ " " + bottles + " of beer on the wall,");
      console.log(i+ " " + bottles + " of beer,");
      console.log("Take one down, pass it around,");
      console.log(bottlesLeft);
      }  
  }
beerSong();


// Add j and another for loop to increase the number of bottle take down