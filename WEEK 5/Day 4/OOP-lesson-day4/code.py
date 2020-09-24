# with open("jaime.txt", "a+") as f:
#     f.write("jaime saucisses2\n")

# def getline(file_path, line_num):
#     with open(file_path , 'r') as f:
#         for i in range(line_num):
#             line = f.readline()
#         return line

# exe_lesson
with open('exe.txt','r') as f:
    # print(f.read())
    # print(f.readline(5))
    character = f.readline()
    print(character[0:5])
