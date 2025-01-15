from datetime import datetime

evszam = False

kor = []

while not evszam:
    evek = int(input("Adj meg születési évszámokat: "))
    kor.append(datetime.now().year - evek)
    valasz = input("Szeretnél még meadni évszámokat?").upper()
    if valasz != "I":
        evszam = True
        break

print(kor)
print(f"A korok száma: {len(kor)}")
print(f"A legnagyobb kor: {max(kor)}")