etel = input("Étel neve: ")
rendelo = input("Étel rendelejőnek neve: ")
ertekeles = int(input("Értékelés (1-5): "))


if ertekeles <= 0:
    print("Az értékelés nem lehet negatív!")
elif ertekeles > 5:
    print("5 pont feletti értékelés nem elfogatható!")
else:
    print("Köszönjük az értékelést!")