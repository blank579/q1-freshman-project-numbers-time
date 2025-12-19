import time
import random
import os 
# os.system('cls')


print("hello and welcome to guessing game")
print("you have a few seconds to answer")
#ask you if  you want to start the game
start=input("would you like to start? (yes/no)").lower().strip()
# makes the code run forever (while True)
while True:

   # if start is yes it will spit out tandom numbers
   if start=="yes":
      numbers = random.choice([150,593,992,757,293,553,575])
      # you get 3 seconds  to see the number
      #it clears the terminal os.system('cls') is to clear the terminal
      print("the number is: ",numbers)
      time.sleep(3)
      os.system('cls')
      #always use int when your working with numbers 
      numberguess=int(input("what numbers did u see:\n >").strip())
      print(numberguess)
      if numberguess == numbers:
         print("you got the number right")

      else:
         print("wrong")

  #if the user says no have a good day 
   elif start=="no":
      print ("have a good day")
   else:
      print("we didnt get that try again")
   #numbers spits out a random number
   #code spits a random code

   #number first then timing
   start2=input("would you like to guess a code insted of a number (yes/no)").lower().strip()
   if start2=="yes":
      # you get a random code 
      code = random.choice(['xxipl','LoSe','rain','lone','q','zzzz'])
      print("the number is: ",code)
      #then have 3seconds to answer 
      #clears the terminal 
      time.sleep(3)  
      os.system('cls')
      # you type in the code you saw
      codeguess=input("what code did u see:\n >").strip()
      print(codeguess)
      if codeguess == code:
         print("you got the code right")
      
   
      
   elif start2=="no":
      print ("have a good day")
      break
   else:
      print("we didnt get that try again")
      continue

   playagain=input("would you like to play again(yes/no)\n>").lower().strip
   if playagain=="yes":
      continue
   elif playagain=="no":
      break
# ends the loop





   # codeguess=input("what code did you see: ").lower().strip()
   # print(codeguess)