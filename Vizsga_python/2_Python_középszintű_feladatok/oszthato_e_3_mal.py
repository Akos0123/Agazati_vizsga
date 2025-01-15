oszthato = []

while len(oszthato) < 5: 
    szam = int(input("Kérek egy számot: "))
    if szam % 3 == 0:
        oszthato.append(szam)

    if len(oszthato) >= 5:
        break

    valasz = input("Szeretnél még számot megadni? (I/N): ").upper()
    if valasz != "I":
        break 

if len(oszthato) >= 5:
    print(f"A lista hossza: {len(oszthato)}")
    print(f"A legkisebb szám a listában: {min(oszthato)}")
else:
    print("Nem adtál meg elegendő számot, ami osztható 3-mal.")

