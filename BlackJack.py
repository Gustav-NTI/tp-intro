import random
kort1 = random.randint(1, 11)
kort2 = random.randint(1, 11)

print(f"Din giv är {kort1} och {kort2}, = {kort1 + kort2}")

if kort1 + kort2 == 21:
    print("Blackjack")

else:
    huset1 = random.randint(1, 11)
    huset2 = random.randint(1, 11)
    print(f"Huset drar {huset1} och {huset2}, = {huset1 + huset2}")

    stanna = "n"
    summa = kort1 + kort2
    while stanna.lower() != "j":
        print(f"Din Totala summa är {summa}")
        stanna = input("Stanna? [J/N]")
        if stanna.lower() != "j":
            break
        else:
            summa += random.randint(1, 11)

    elif summa == 21:
    print("BlackJack")
        break
    elif summa > 21:
        print("Bust")
        break
else: summa += random.randint(1, 11)

stanna = input("Stanna? [J/N]")
if stanna.lower() == "j":
        print(f"Du stannar på {summa}")
        break
    else:
        
  huset = huset1 + huset2
  if summa < 21:
    while huest < 17:
      huset += random.randint(1, 11)  
      print(f"Huset har {huset}")
  
  if huset == 21 or huset > summa and huset < 22:
      print("Huset vann fick blackjack")
    elif huset == summa:
      print("lika, try again")
    elif:
        print("Du vinner")


    
