import time
import random
import os
import getpass


def apply_damage(health, damage):
    health -= damage
    if health < 0:
        health = 0
    return health



def clear():
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

health = 100
level=0
correct_answer=0
print(f"\nLEVEL: {level}")

print(" you have health", health)
print("hello and welcome to guessing game")
print("you have a few seconds to answer")
print("you got lucky today you have a vault to open and might get a suprise")

start = input("would you like to start? (yes/no) ").lower().strip()

if start != "yes":
    print("have a good day")
    exit()


while health > 0:
   print(f"\n LEVEL: {level}")

   random_goodvandingMachine = random.choice(
      ["energy drink", "water", "milk", "coffee", "golden apple"]
   )

   random_goodvandingMachine2 = random.choice(
      ["protein bar", "pizza", "potion", "big potion", "bandage", "magic potion", "burger"]
   )

   random_cursedvandingMachine = random.choice(
      ["sleepy drink", "explosive drink", "dark exiler", "cursed coffee"]
   )

   random_cursedvandingMachine2 = random.choice(
      ["grim reapear", "rotten milk", "cursed milk", "trap juice box", "posion drink"]
   )

   random_goodluck = random.choice(
      ["valut", "money", "new shoes", "new car", "teddy bear", "new phone"]
   )
# level system will be next to add like the more questions u get right the more harder u get 
   
   numbers = random.choice([1504, 5991, 9945, 7561, 2921, 5311, 5761])
   if level==0:
       numbers= random.randint(1000,9999)

   elif level==1:
       numbers=random.randint(10000,99999)


   elif level==2:
       numbers=random.randint(100000,999999)

   
   elif level==3:
       numbers=random.randint(10000000,9999999)

   print("\nthe number is:", numbers)
   clear()


   numberguess = int(input("\n\n\n\n\nwhat number did you see: "))


   if numberguess == numbers:

      print("you got the number right")
      correct_answer+=1
      if correct_answer % 3 ==0 and level <3:
          level +=1
          print(f" LEVEL UP ! You are now level {level}")
          if level ==3:
              print("you have reached max level")

      print("you got", random_goodluck)
      print("you got", random_goodvandingMachine)

      if random_goodvandingMachine == "energy drink":
         healed = random.randint(15, 17)
         health += healed
         print(f" you got healed by energy drink {healed} health")

      elif random_goodvandingMachine == "water":
         healed = random.randint(5, 7)
         health += healed
         print(f" you got healed by water {healed} health")

      elif random_goodvandingMachine == "coffee":
         healed = random.randint(1, 2)
         health += healed
         print(f" you got healed by coffee {healed} health")
      
      elif random_goodvandingMachine == "milk":
         healed = random.randint(3, 9)
         health += healed
         print(f" you got healed by milk {healed} health")
      
      elif random_goodvandingMachine == "golden apple":
         healed = random.randint(50, 57)
         health += healed
         print(f" you got healed by golden apple {healed} health")

      if health > 100:
         health = 100
      print("you have max hp",health)
         

   elif numberguess != numbers:

      print("wrong!")
   


      random_badluck = random.choice(["traps", "spikes", "lasers"])
      print("you got hit by:", random_badluck)
      print("cursed effect:", random_cursedvandingMachine)

      if random_badluck == "traps":
         damage = random.randint(45, 50)
         health = apply_damage(health, damage)
                                                                                                             
          
         print(f"TRAPS dealt {damage} damage")

      elif random_badluck == "spikes":
         damage = random.randint(25, 30)
         health = apply_damage(health, damage)
         
         print(f"SPIKES dealt {damage} damage")

      elif random_badluck == "lasers":
         damage = random.randint(55, 77)
         health = apply_damage(health, damage)
        
         print(f"LASERS dealt {damage} damage")

      print("health after damage:", health)

      if health <= 0:
         print("you died game over")
         break

     
      if random_cursedvandingMachine == "explosive drink":
         damage = random.randint(35, 37)
         health = apply_damage(health, damage)
         
         print(f"explosive drink hit you for {damage} damage")

      elif random_cursedvandingMachine == "dark exiler":
         damage = random.randint(50, 57)
         health = apply_damage(health, damage)
         
         print(f"dark exiler hit you for {damage} damage")

      elif random_cursedvandingMachine == "cursed coffee":
         damage = random.randint(25, 27)
         health = apply_damage(health, damage)
         
         print(f"cursed coffee hit you for {damage} damage")

      elif random_cursedvandingMachine == "sleepy drink":
         damage = random.randint(55, 60)
         health = apply_damage(health, damage)
    
         print(f"sleepy drink hit you for {damage} damage")

      print("health after cursed machine:", health)

      if health <= 0:
         print("you died! game over")
         break

  
   start2 = input("\nwould you like to guess a code instead? (yes/no) ").lower().strip()

   if start2 == "yes":

      code = random.choice(['xipll', 'losey', 'rainy', 'lonely', 'euww', 'zzzs'])

      print("code is:", code)
      time.sleep(2)
      os.system("clear")

      codeguess = input("what code did you see: ")

      if codeguess == code:
         

         print("you got the code right")
         correct_answer+=1
         if correct_answer %3 == 0 and level < 3:
             level +=1
             print(f" LEVEL UP! You are now level {level}")
         print("you got", random_goodluck)
         
         
       
         print("you got:", random_goodvandingMachine2)
         if random_goodvandingMachine2 == "protein bar":
            healed = random.randint(20, 24)
            health += healed
            print(f" you got healed by protein bar {healed} health")
         elif random_goodvandingMachine2 == "pizza":
            healed = random.randint(5, 9)
            health += healed
            print(f" you got healed by pizza {healed} health")
         elif random_goodvandingMachine2 == "potion":
            healed = random.randint(10, 12)
            health += healed
            print(f" you got healed by potion {healed} health")
         elif random_goodvandingMachine2 == "big potion":
            healed = random.randint(55, 77)
            health += healed
            print(f" you got healed by big potion {healed} health")
         elif random_goodvandingMachine2 == "bandage":
            healed = random.randint(10, 14)
            health += healed
            print(f" you got healed by bandage {healed} health")
         elif random_goodvandingMachine2 == "magic potion":
            healed= random.randint(57, 75)
            health += healed
            print(f" you got healed by magic potion {healed} health")
         elif random_goodvandingMachine2 == "burger":
            healed = random.randint(20, 24)
            health += healed
            print(f" you got healed by burger {healed} health")
         if health > 100:
            health = 100
         print("health after heal:", health)
         print("you win")
      elif codeguess != code:
         random_badluck = random.choice(["traps", "spikes", "lasers"])
         print("you got hit by:", random_badluck)
         print("cursed effect:", random_cursedvandingMachine2)
             
         if random_badluck == "traps":
               damage = random.randint(45, 50)
               health = apply_damage(health, damage)
               print(f"code fail TRAPS dealt {damage} damage") 

         elif random_badluck == "spikes":
               damage = random.randint(25, 30)
               health = apply_damage(health, damage)
               print(f"code fail SPIKES dealt {damage} damage")

         elif random_badluck == "lasers":
               damage = random.randint(90, 95)
               health = apply_damage(health, damage)
               print(f"code fail LASERS dealt {damage} damage")

         print("health after code round:", health)


      

         if random_cursedvandingMachine2=="grim reapear":
              damage = random.randint(1, 100)
              health = apply_damage(health, damage)
              print(f" grim reapear took your soul {damage} damage")

         elif random_cursedvandingMachine2=="rotten milk":
                damage = random.randint(2, 4)
                health = apply_damage(health, damage)
                print(f" rotten milk hit for {damage} damage")

         elif random_cursedvandingMachine2=="cursed milk":
                damage = random.randint(20, 40)
                health = apply_damage(health, damage)
                print(f" you got cursed milk  {damage} damage")

         elif random_cursedvandingMachine2=="trap juice box":
                damage = random.randint(45, 50)
                health = apply_damage(health, damage)
                print(f" you got trap juice box {damage} damage")

         elif random_cursedvandingMachine2=="posion drink":
              damage = random.randint(45, 50)
              health = apply_damage(health, damage)
              print(f" posion drink  {damage} damage")
              print("health after final code round:", health)
             




         if health <= 0:
               print("you died better luck next time")
               break

   elif start2 == "no":
      print("have a good day")
      break

   else:
      print("we didnt get that try again")
      continue

 
   print("\n=== END OF ROUND ===")
   print("final health after all damage:", health)

   playagain = input("play again? (yes/no): ").lower().strip()

   if playagain != "yes":
      break

   print("\nGame Over")

print("\nGame Over")
print("your final health was:", health)
hidden_name = getpass.getpass("  ")

print(f"Name received! (Hidden from terminal view)")


















































































































# import time
# import random
# import os 
# # os.system('cls')


# print("hello and welcome to guessing game")
# print("you have a few seconds to answer")
# #ask you if  you want to start the game
# start=input("would you like to start? (yes/no)").lower().strip()
# # makes the code run forever (while True)
# while True:

#    # if start is yes it will spit out tandom numbers
#    if start=="yes":
#       numbers = random.choice([150,593,992,757,293,553,575])
#       # you get 3 seconds  to see the number
#       #it clears the terminal os.system('cls') is to clear the terminal
#       print("the number is: ",numbers)
#       time.sleep(3)
#       os.system('cls')
#       #always use int when your working with numbers 
#       numberguess=int(input("what numbers did u see:\n >").strip())
#       print(numberguess)
#       if numberguess == numbers:
#          print("you got the number right")

#       else:
#          print("wrong")

#   #if the user says no have a good day 
#    elif start=="no":
#       print ("have a good day")
#    else:
#       print("we didnt get that try again")
#    #numbers spits out a random number
#    #code spits a random code

#    #number first then timing
#    start2=input("would you like to guess a code insted of a number (yes/no)").lower().strip()
#    if start2=="yes":
#       # you get a random code 
#       code = random.choice(['xxipl','LoSe','rain','lone','q','zzzz'])
#       print("the number is: ",code)
#       #then have 3seconds to answer 
#       #clears the terminal 
#       time.sleep(3)  
#       os.system('cls')
#       # you type in the code you saw
#       codeguess=input("what code did u see:\n >").strip()
#       print(codeguess)
#       if codeguess == code:
#          print("you got the code right")
      
   
      
#    elif start2=="no":
#       print ("have a good day")
#       break
#    else:
#       print("we didnt get that try again")
#       continue

#    playagain=input("would you like to play again(yes/no)\n>").lower().strip
#    if playagain=="yes":
#       continue
#    elif playagain=="no":
#       break
# # ends the loop





#    # codeguess=input("what code did you see: ").lower().strip()
#    # print(codeguess)