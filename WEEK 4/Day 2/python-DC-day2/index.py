birthday = input("Type your date birth (DD/MM/YEAR)")
birthday.strip()
day, month, year = birthday.split("/")

calculate_age = 2020 - int(year) 
number_of_candle = str(calculate_age)[1]

print(calculate_age)
print(number_of_candle)


if int(year) % 4 == 0 or int(year) % 100 == 0:
    for candle in number_of_candle:
        candle = "i"*int(candle)
    print("    ___",candle,"___")
    print("   |:H:a:p:p:y:|\n __|___________|__\n|^^^^^^^^^^^^^^^^^|\n|:B:i:r:t:h:d:a:y:|\n|                 |\n~~~~~~~~~~~~~~~~~~~\n")
    
    print("Cake for LEAP")
    print("    ___",candle,"___")
    print("   |:H:a:p:p:y:|\n __|___________|__\n|^^^^^^^^^^^^^^^^^|\n|:B:i:r:t:h:d:a:y:|\n|                 |\n~~~~~~~~~~~~~~~~~~~")

else:
    for candle in number_of_candle:
        candle = "i"*int(candle)
    print("     ___",candle,"___")
    print("   |:H:a:p:p:y:|\n __|___________|__\n|^^^^^^^^^^^^^^^^^|\n|:B:i:r:t:h:d:a:y:|\n|                 |\n~~~~~~~~~~~~~~~~~~~")
 
    






       
#        ___iiiii___




#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~
