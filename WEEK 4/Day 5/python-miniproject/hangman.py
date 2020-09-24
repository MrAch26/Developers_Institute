import random 
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_complete = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_word = []
    lives = 6

    print("\nWelcome to my 'Hangman' Game")
    print(f'You are starting with {lives} Lives')
    print(word_complete,"\n")

    while not guessed and lives > 0:
        try1 = input('Type in a letter or word: ').upper()
        if len(try1) == 1 and try1.isalpha():
            if try1 in guessed_letters:
                print("You already typed this letter")
            elif try1 not in word:
                print(try1,'Is not is the word')
                lives -= 1
                guessed_letters.append(try1) 
            else:
                print("great",try1,"is in the word")
                guessed_letters.append(try1)
                word_as_list = list(word_complete)
                indices = [i for i, letter in enumerate(word) if letter == try1]
                for index in indices:
                    word_as_list[index] = try1
                word_complete = "".join(word_as_list)
                if "_" not in word_complete:
                    guessed = True
                
        elif len(try1) == len(try1) and try1.isalpha():
            if try1 in guessed_word :
                print("You've already typed this word")
            elif try1 != word:
                print("nope",try1,"is not the word")
                guessed_word.append(try1)
                lives-=1
            else:
                print('YES YOU GOT IT !')
                guessed = True
                word_complete = word


            
        else: 
            print("Invalid try again")
        print(lives, 'left')
        print(word_complete,'\n')\
# if guessed is true 
    if guessed:
        print("You guessed the word you won !")
    else :
        print("Sorry you lost go buy yourself another brain\n the word was",word)

def main():
    word = get_word()
    play(word)
    while input("Play Again ? (Y/N)").upper() == 'Y':
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()