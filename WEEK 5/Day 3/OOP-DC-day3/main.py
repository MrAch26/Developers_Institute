
# class Is_Palindrome():
#     def __init__(self,word):
#         self.word = word
    
#     def __repr__(self):
#         if self.word == self.word[::-1]:
#             # print(f"{self.word} is a Palindrome")
#             return f"True, {self.word} is a Palindrome"
#         else:
#             # print(f"{self.word} is NOT a Palindrome")
#             return f"False, {self.word} is NOT a Palindrome"

# def main():
#     word = Is_Palindrome("kayak")
#     print(word)

# if __name__ == '__main__':
#     main()
    

class Palindrome():
    def checker(word):
        return word == word[::1]

word = Palindrome.checker("")
print(word)