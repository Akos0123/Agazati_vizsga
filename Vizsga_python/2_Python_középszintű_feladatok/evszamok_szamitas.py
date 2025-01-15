megad = False

evszamok = []

while not megad:
    evszam = input("Adj meg évszámokat: ")
    if evszam.isdigit():
        evszamok.append(int(evszam))
    else:
        print("Nem évszámot adtál meg.")
        break
    valasz = input("Szeretnél még évszámot hozzáadni? (I/N): ").upper()
    if valasz != "I":
        megad = True

print(f"A legidősebb kor: {max(evszamok)}")
alatti = [ev for ev in evszamok if ev < 2000]
evszamok.sort()
print(f"A 2000 alatti évszámok: {alatti}")
print(f"A listában {len(evszamok)} db van.")