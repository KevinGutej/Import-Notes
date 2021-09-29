''''''#Additional modules in python.
#import copy, We can make another copy of the object
# e.g
# import copy
# class animal:
#     def init(self, gatunek, liczba_nóg, kolor):
#       self.gatunek = gatunek
#       self.liczba_nóg = liczba_nóg
#       self.kolor = kolor
# kevin = animal('pig',6,'red')
# kevin = copy.copy(kevin)
# print(kevin.animal)
# print(kevin.animal)
#
# kevin = animal('pig',6,'red')
# my_animals = [kevin,kevin,kevin]
# more_animals = copy.copy(my_animals)
#
# my_animals[0].gatunek ='ghul'
# print(my_animals[0].gatunek)
#
# more_animals=copy.deepcopy(my_animals)

# import keyword
# print(keyword.iskeyword('if'))
#ouput = True
# print(keyword.iskeyword('oswald'))
#output = False
# print(keyword.kwlist)

# import random
# print(random.randint(100,1000))

# import random
# fruits = ['apple','banana','orange']
# print(random.choice(fruits))
# random.shuffle(fruits)
# print(fruits)

import time
#print(time.time())
# def alot_numbers(max):
#     t1 = time.time()
#     for x in range(0,max):
#         print(x)
#     t2 = time.time()
#     print('uplynelo %s skund'% (t2-t1))
#
# alot_numbers(1000)

# import time
# print(time.asctime())

# import time
# print(time.localtime())

# t = time.localtime()
# time = t[3]
# month = t[1]
# print(time)
# print(month)

# for x in range(1, 61):
#     print(x)
#     time.sleep(2)

# import pickle
# stan_gry = {
#     'pozycja-gracza':'N23 E45',
#     'kieszenie':['klucze','scyzoryk','otoczak'],
#     'plecak':['lina','mlotek','jablko'],
#     'pieniadze': 158.50
# }
# plik_zapisu = open('save.dat','wb')
# pickle.dump(stan_gry,plik_zapisu)
# plik_zapisu.close()
#
# wczytywany_plik = open('save.dat','rb')
# wczytane_dane_gry = pickle.load(wczytywany_plik)
# wczytywany_plik.close()
# print(wczytane_dane_gry)



#1.)
# import copy
# class Auto:
#     pass
# auto1 = Auto()
# auto1.koła = 4
# auto2 = auto1
# auto2.koła = 3
# print(auto1.koła)
#
#
# auto3 = auto1
# auto3.koła = 6
# print(auto1.koła)

# Create a list of your favorite things then use the pickle function, to save them to a file called favorites.dat.
# Close the program, then rerun and list your favorite stuff by loading this file.
# import pickle
# favourite_things = {
#     'car' : 'lambo',
#     'console' : 'ps4',
#     'food' : 'fruits'
# }
# plik_zapisu = open('favorites.dat','wb')
# pickle.dump(favourite_things,plik_zapisu)
# plik_zapisu.close()
# wczytywany_plik = open('favorites.dat','rb')
# wczytane_dane_gry = pickle.load(wczytywany_plik)
# wczytywany_plik.close()
# print(wczytane_dane_gry)

#Create program that will roll the dice. It should draw a different number each time.
# import random
# print(random.randint(0,6))


# import copy
# Ronaldo = {
#     'Shooting': '98',
#     'Passing': '89',
#     'Dribbiling': '95',
#     'Defending': '56',
#     'Heading': '78'
#
# }
# Lewandowski = copy.copy(Ronaldo)
# print(Lewandowski)

# Create program that will count to 100 then print the word "BREAK!" 5 times.
# how long your computer will carry out this operation? Send your code to teacher and compare your results.
# import time
# t1 = time.time()
# for k in range(0,6):
#     for x in range(0,101):
#         print(x)
#
#     print("BREAK!")
# t2 = time.time()
# print(t2 - t1)
#
#
#
#
#
# keywords = ['name','age','surname','gender']
# if input word not in keyword:


import keyword
key_word = input()
if keyword.iskeyword(key_word):
    print("You can't use it.")
else:
    print("You can use it.")





























''''''