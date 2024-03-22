import win32com.client
from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice").Speak
import random
from random import *

lst = ["stone", "paper", "scissor"]
dic = {"stone": r'''
        ▓▓████████                  
        ██    ░░░░▓▓██                
     ██      ▒▒░░░░▓▓████            
     ██      ▒▒▒▒▒▒    ▓▓██
        | |                  
     ___| |_ ___  _ __   ___ 
    / __| __/ _ \| '_ \ / _ \
    \__ \ || (_) | | | |  __/
    |___/\__\___/|_| |_|\___|
                         
''',
       "paper": r'''
     ----------------
    |-----------------|
    |-----------------|
    |-----------------|
    |-----------------|
    |-----------------|
    |-----------------|
     -----------------       
         _ __   __ _ _ __   ___ _ __ 
        | '_ \ / _` | '_ \ / _ \ '__|
        | |_) | (_| | |_) |  __/ |   
        | .__/ \__,_| .__/ \___|_|   
        | |         | |              
        |_|         |_|       
''',
       "scissor": r'''

    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.

         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \
|___/\___|_|___/___/\___/|_|  |___/
                                   
                                          
'''

       }

count = 0
score = 0
print(r'''
            .-"""-.
           /       \
           \       /
    .-"""-.-`.-.-.<  _
   /      _,-\ ()()_/:)
   \     / ,  `     `|
    '-..-| \-.,___,  /
          \ `-.__/  /
     jgs / `-.__.-\`
        / /|    ___\
       ( ( |.-"`   `'\
        \ \/    {}{}  |
         \|           /
          \        , /
          ( __`;-;'__`)
          `//'`   `||`
         _//       ||
 .-"-._,(__)     .(__).-""-.
/          \    /           \
\          /    \           /
 `'-------`      `--------'`
    ''')
speak("welcome to stone paper and scissor,i am your host Mickey mouse.. ")
speak("lets play the game.first you will give input:")
while count <= 3:
    print("stone , paper or scissor:")
    opt = input()
    print("your choice:")
    print(dic[f"{opt}"])
    cho = choice(lst)
    print("Mickys choice:")
    print(dic[f"{cho}"])
    if opt == cho:
        print("tie")
    elif opt == "stone" and cho == "paper":
        print("you lost")
        count += 1
    elif opt == "stone" and cho == "scissor":
        print("you won")
        score = score + 10
        print("your core is ", score)
    elif opt == "scissor" and cho == "paper":
        print("you won")
        score = score + 10
        print("your core is ", score)
    elif opt == "paper" and cho == "scissor":
        print("you lost")
        count += 1
    elif opt == "paper" and cho == "stone":
        print("you won")
        score = score + 10
        print("your core is ", score)
    elif opt == "scissor" and cho == "stone":
        print("you lost")
        count += 1

print(f"you lost with score :{score}")