name = input("ENTER YOUR NAME: ")
print(f"\n---------HELLO {name}--------\n-----LET'S PLAY A GAME-----\n")
print("GAME IS CALLED:\nGUESS THE NUMBER\n")
correct_number = 5 
for attempt in range(3):
  user_input = int(input("GUESS A NUMBER BETWWEEN 1 TO 10:"))
  if user_input == correct_number:
    print("YOU GUESSED IT RIGHT!! \nYOU WON THE GAME!! \nCONGRATULATIONS!")
    break
  else:
    print(f"YOU GUEESED IT WRONG!! \nTRY AGAIN. \nAttempts left: {2 - attempt}\n")
else:
  print("YOU LOST THE GAME!! \nBETTER LUCK NEXT TIME")
