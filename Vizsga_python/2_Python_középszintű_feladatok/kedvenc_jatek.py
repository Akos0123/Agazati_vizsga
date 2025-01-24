import random
jatekok = []
darab = 0 
while True:
    jatek = input("Add meg a kedvenc vidójátékodat:")
    jatekok.append(jatek)
    darab += 1
    print(f"{darab}.játék:{jatek}")
    if darab == 4: 
        break
print(f"{";".join (map(str,jatekok))}")

kedvenc = random.choice(jatekok)
print(f"A kedvenc játékok {kedvenc}")
