import time
import random
import os


def apply_damage(health, damage):
    health -= damage
    if health < 0:
        health = 0
    return health


def clear():
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')


health = 100
level = 0
correct_answer = 0
coins = 0

print(f"\nLEVEL: {level}")
print("You have health:", health)
print("Hello and welcome to the guessing game!")
print("You have a few seconds to remember the number or code.")
print("You got lucky today! You have a vault to open and might get a surprise.")

start = input("Would you like to start? (yes/no) ").lower().strip()

if start != "yes":
    print("Have a good day!")

else:
    while health > 0:
        print(f"\nLEVEL: {level}")
        print("Health:", health)
        print("Coins:", coins)

        random_goodvandingMachine = random.choice(
            ["energy drink", "water", "milk", "coffee", "golden apple"]
        )

        random_goodvandingMachine2 = random.choice(
            ["protein bar", "pizza", "potion", "big potion",
             "bandage", "magic potion", "burger"]
        )

        random_cursedvandingMachine = random.choice(
            ["sleepy drink", "explosive drink", "dark exiler", "cursed coffee"]
        )

        random_cursedvandingMachine2 = random.choice(
            ["grim reapear", "rotten milk", "cursed milk",
             "trap juice box", "posion drink"]
        )

        random_goodluck = random.choice(
            ["vault", "money", "new shoes", "new car", "teddy bear", "new phone"]
        )

        # NUMBER DIFFICULTY

        if level == 0:
            numbers = random.randint(1000, 9999)
            print("LEVEL Difficulty: EASY")
            coins_earned = random.randint(80, 100)

        elif level == 1:
            numbers = random.randint(10000, 99999)
            print("LEVEL Difficulty: MEDIUM")
            coins_earned = random.randint(57, 75)

        elif level == 2:
            numbers = random.randint(100000, 999999)
            print("LEVEL Difficulty: HARD")
            coins_earned = random.randint(25, 27)

        else:
            numbers = random.randint(10000000, 99999999)
            print("LEVEL Difficulty: EXTREME")
            coins_earned = random.randint(15, 17)

        print("\nThe number is:", numbers)
        clear()

        # NUMBER INPUT VALIDATION

        while True:
            try:
                numberguess = int(input("\nWhat number did you see? "))
                break
            except ValueError:
                print("Only enter numbers. Try again.")

        if numberguess == numbers:
            print("You got the number right!")

            coins += coins_earned
            print(f"+ {coins_earned} coins!")
            print(f"Total coins: {coins}")

            correct_answer += 1

            if correct_answer % 3 == 0 and level < 3:
                level += 1
                print(f"LEVEL UP! You are now level {level}")

                if level == 3:
                    print("You have reached max level!")

            print("You got:", random_goodluck)
            print("You got:", random_goodvandingMachine)

            if random_goodvandingMachine == "energy drink":
                healed = random.randint(15, 17)
                health += healed
                print(f"Energy drink healed you by {healed} health.")

            elif random_goodvandingMachine == "water":
                healed = random.randint(5, 7)
                health += healed
                print(f"Water healed you by {healed} health.")

            elif random_goodvandingMachine == "coffee":
                healed = random.randint(1, 2)
                health += healed
                print(f"Coffee healed you by {healed} health.")

            elif random_goodvandingMachine == "milk":
                healed = random.randint(3, 9)
                health += healed
                print(f"Milk healed you by {healed} health.")

            elif random_goodvandingMachine == "golden apple":
                healed = random.randint(50, 57)
                health += healed
                print(f"Golden apple healed you by {healed} health.")

            if health > 100:
                health = 100

            print("Health after healing:", health)

        else:
            print("Wrong!")

            random_badluck = random.choice(["traps", "spikes", "lasers"])
            print("You got hit by:", random_badluck)
            print("Cursed effect:", random_cursedvandingMachine)

            if random_badluck == "traps":
                damage = random.randint(45, 50)
                health = apply_damage(health, damage)
                print(f"TRAPS dealt {damage} damage.")

            elif random_badluck == "spikes":
                damage = random.randint(25, 30)
                health = apply_damage(health, damage)
                print(f"SPIKES dealt {damage} damage.")

            else:
                damage = random.randint(55, 77)
                health = apply_damage(health, damage)
                print(f"LASERS dealt {damage} damage.")

            print("Health after damage:", health)

            if health <= 0:
                print("You died! Game over.")
                break

            if random_cursedvandingMachine == "explosive drink":
                damage = random.randint(35, 37)
                health = apply_damage(health, damage)
                print(f"Explosive drink hit you for {damage} damage.")

            elif random_cursedvandingMachine == "dark exiler":
                damage = random.randint(50, 57)
                health = apply_damage(health, damage)
                print(f"Dark exiler hit you for {damage} damage.")

            elif random_cursedvandingMachine == "cursed coffee":
                damage = random.randint(25, 27)
                health = apply_damage(health, damage)
                print(f"Cursed coffee hit you for {damage} damage.")

            elif random_cursedvandingMachine == "sleepy drink":
                damage = random.randint(55, 60)
                health = apply_damage(health, damage)
                print(f"Sleepy drink hit you for {damage} damage.")

            print("Health after cursed machine:", health)

            if health <= 0:
                print("You died! Game over.")
                break

        # CODE GUESSING

        while True:
            start2 = input(
                "\nWould you like to guess a code too? (yes/no) "
            ).lower().strip()

            if start2 in ["yes", "no"]:
                break

            print("Please enter yes or no.")

        if start2 == "yes":

            if level == 0:
                code = random.choice(
                    ["light", "dark", "mundane", "rainnnny day"]
                )
                print("LEVEL Difficulty: EASY")
                coins_earned = random.randint(50, 70)

            elif level == 1:
                code = random.choice(
                    ["zzzzzz", "Eclipse Moon", "Night falll"]
                )
                print("LEVEL Difficulty: MEDIUM")
                coins_earned = random.randint(44, 49)

            elif level == 2:
                code = random.choice(
                    ["ckasechkenx", "wodahS", "vortex$57"]
                )
                print("LEVEL Difficulty: HARD")
                coins_earned = random.randint(10, 15)

            else:
                code = random.choice(
                    ["gggg", "u_seen", "tim#_tamp", "Sentinelx,XTREAM"]
                )
                print("LEVEL Difficulty: EXTREME")
                coins_earned = random.randint(1, 5)

            print("Code is:", code)
            clear()

            codeguess = input("What code did you see? ").strip()

            if codeguess == code:
                print("You got the code right!")

                coins += coins_earned
                print(f"+ {coins_earned} coins!")
                print(f"Total coins: {coins}")

                correct_answer += 1

                if correct_answer % 3 == 0 and level < 3:
                    level += 1
                    print(f"LEVEL UP! You are now level {level}")

                    if level == 3:
                        print("You have reached max level!")

                print("You got:", random_goodluck)
                print("You got:", random_goodvandingMachine2)

                if random_goodvandingMachine2 == "protein bar":
                    healed = random.randint(20, 24)
                    health += healed
                    print(f"Protein bar healed you by {healed} health.")

                elif random_goodvandingMachine2 == "pizza":
                    healed = random.randint(5, 9)
                    health += healed
                    print(f"Pizza healed you by {healed} health.")

                elif random_goodvandingMachine2 == "potion":
                    healed = random.randint(10, 12)
                    health += healed
                    print(f"Potion healed you by {healed} health.")

                elif random_goodvandingMachine2 == "big potion":
                    healed = random.randint(55, 77)
                    health += healed
                    print(f"Big potion healed you by {healed} health.")

                elif random_goodvandingMachine2 == "bandage":
                    healed = random.randint(10, 14)
                    health += healed
                    print(f"Bandage healed you by {healed} health.")

                elif random_goodvandingMachine2 == "magic potion":
                    healed = random.randint(57, 75)
                    health += healed
                    print(f"Magic potion healed you by {healed} health.")

                elif random_goodvandingMachine2 == "burger":
                    healed = random.randint(20, 24)
                    health += healed
                    print(f"Burger healed you by {healed} health.")

                if health > 100:
                    health = 100

                print("Health after healing:", health)
                print("You win!")

            else:
                print("Wrong code!")

                random_badluck = random.choice(
                    ["traps", "spikes", "lasers"]
                )

                print("You got hit by:", random_badluck)
                print("Cursed effect:", random_cursedvandingMachine2)

                if random_badluck == "traps":
                    damage = random.randint(45, 50)
                    health = apply_damage(health, damage)
                    print(f"Code fail: TRAPS dealt {damage} damage.")

                elif random_badluck == "spikes":
                    damage = random.randint(25, 30)
                    health = apply_damage(health, damage)
                    print(f"Code fail: SPIKES dealt {damage} damage.")

                else:
                    damage = random.randint(90, 95)
                    health = apply_damage(health, damage)
                    print(f"Code fail: LASERS dealt {damage} damage.")

                print("Health after code round:", health)

                if health > 0:

                    if random_cursedvandingMachine2 == "grim reapear":
                        damage = random.randint(1, 100)
                        health = apply_damage(health, damage)
                        print(f"Grim reapear dealt {damage} damage.")

                    elif random_cursedvandingMachine2 == "rotten milk":
                        damage = random.randint(2, 4)
                        health = apply_damage(health, damage)
                        print(f"Rotten milk dealt {damage} damage.")

                    elif random_cursedvandingMachine2 == "cursed milk":
                        damage = random.randint(20, 40)
                        health = apply_damage(health, damage)
                        print(f"Cursed milk dealt {damage} damage.")

                    elif random_cursedvandingMachine2 == "trap juice box":
                        damage = random.randint(45, 50)
                        health = apply_damage(health, damage)
                        print(f"Trap juice box dealt {damage} damage.")

                    elif random_cursedvandingMachine2 == "posion drink":
                        damage = random.randint(45, 50)
                        health = apply_damage(health, damage)
                        print(f"Poison drink dealt {damage} damage.")

                print("Health after final code round:", health)

                if health <= 0:
                    print("You died! Better luck next time.")
                    break

        else:
            print("Have a good day!")
            break

        print("\n=== END OF ROUND ===")
        print("Final health after all damage:", health)
        print("Total coins:", coins)

        if health <= 0:
            break

        while True:
            playagain = input("Play again? (yes/no): ").lower().strip()

            if playagain in ["yes", "no"]:
                break

            print("Please enter yes or no.")

        if playagain == "no":
            break

print("\nGame Over")
print("Your final health was:", health)
print("Your final coins:", coins)











































































































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