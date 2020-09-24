# # XP
# # EXE 1

# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# def findOld(*cats):

#     max = cats[0].age
#     for i in range(len(cats)):
#         if cats[i].age > max:
#             max = cats[i].age

#     print(cats[i].name,'is the oldest cat :) ')


# def main():
#     cat0 = Cat("popi",1)
#     cat1 = Cat("papi",3)
#     cat2 = Cat("momi",6)

#     findOld(cat0,cat1,cat2)

# if __name__ == '__main__':
#     main()

# DONE WITH JULIEN COHEN merci
# # EXE 2
# class Dog():
#
#     def __init__(self, nameDog, heightDog):
#         self.nameDog = nameDog
#         self.heightDog = heightDog
#
#     def talk(self):
#         print("WOUAF !")
#
#     def jump(self):
#         height2 = self.heightDog * 2
#         print(f'When {self.nameDog} is jumping his height is {height2} cm')
#
#     def infos(self):
#         print(f"The name is {self.nameDog}, and the height is {self.heightDog} cm")
#
#
# def main():
#     davids_dog = Dog("Rex", 50)
#     sarahs_dog = Dog("Teacup", 20)
#     davids_dog.infos()
#     davids_dog.jump()
#     sarahs_dog.infos()
#
#     if davids_dog.heightDog > sarahs_dog.heightDog:
#         print(f"{davids_dog.nameDog} is bigger !")
#     else:
#         print('The other dog is taller')
#
#
# if __name__ == '__main__':
#     main()

# # EXE 3
#
# class Song:
#     def __init__(self, lyrics=[]):
#         self.lyrics = lyrics
#
#     def sing_me_a_song(self):
#         for e in map(str, self.lyrics):
#             print(e)
#
#
# def main():
#     happy_bday = Song(["Have a sunshine on you, Happy Birthday to you !"])
#     happy_bday.sing_me_a_song()
#
#
# if __name__ == '__main__':
#     main()

# # EXE 4
# class Zoo:
#     def __init__(self,zoo_name):
#         self.zoo_name = zoo_name
#
    # def