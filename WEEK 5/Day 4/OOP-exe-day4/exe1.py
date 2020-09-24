import random


def get_words_from_file(file):
    with open(file, 'r+') as f:
        return f.readlines()


def get_random_sentence(length):
    while length not in range(2, 21):
        length = int(input('it must be beetween 2 and 20 words'))

    else:
        sentence = []
        for i in range(length):
            list26 = get_words_from_file('list1.txt')
            list26 = list(map(lambda s: s.strip(), list26))
            list26 = list(map(lambda s: s.lower(), list26))
            random_word = random.choice(list26)

            sentence.append(random_word)
        print(' '.join(sentence))


def main():
    print('This is a program that will generate a random sentence and display it to the user.'
          'We will allow the user to choose how long the sentence will be.\n')
    length = int(input("How many word do you want in your sentence ?"))
    get_random_sentence(length)


if __name__ == '__main__':
    main()
