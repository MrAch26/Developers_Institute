import self as self


class Text:
    def __init__(self):
        with open("the_stranger.txt", "r") as text:
            self.list1 = text.readlines()
            self.list1 = list(map(lambda s: s.strip(), self.list1))


        with open("the_stranger.txt", "r") as text:
            self.string = text.read()

    def freq(self):
        str_list = self.string.split()
        unique_words = set(str_list)
        print('checking for word')
        for words in unique_words:
            if str_list.count(words) > 1500:
                print('The most common word is', words.upper(), 'and returns', str_list.count(words), 'times.')

    def most_common_word(self):
        from collections import Counter
        Counter = Counter(self.list1)
        most_occur = Counter.most_common(len(self.list1))
        if Counter.most_common() > 1000:
            print(most_occur)

    @classmethod
    def from_file(cls,file):
        with open(file) as f:
            print(f.read())




# class TextModification(Text):

def main():
    t = Text()
    # print(t.name)
    t.freq()
    # Text.from_file('my_text.txt')
    # t.most_common_word()

if __name__ == '__main__':
    main()