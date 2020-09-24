# DAILY CHALLENGE 1
def reverse_Bits(n):
        result = 0
        for i in range(32):
            result <<= 1
            result |= n & 1
            n >>= 1
        return result
            
print(reverse_Bits(1234))

# https://www.w3resource.com/python-exercises/challenges/1/python-challenges-1-exercise-19.php

#  2nd method
input = 1234
binary = "{:032b}".format(input)
binary = binary[::-1]
output = int(binary,2)
print (output)

# 2
s = input("String: ")
ch = input("Character: ")
#{Write your code here
for i in s:
  counter = s.count(ch)
  print(counter)
  break


# 3
print('start')
for i in range(6):
  for j in range(6):
    print(i,j)
    if i+j != j+i:
      print (j,i)