# # 3.Feladat
# # Olvasd be és tárold el az ajandek lista tartalmát. Írask ki a lista teljes tartalmát. A legfiatalabb személynek írd ki a nevét és korát. 
# # Írd ki, hány db kategória van a listában, ismétlés nélkül. Jelenítsd meg a konzolon a személyek neveit, az összeget és akciós árakat, mindenkinél egységesen 20% a kedvezmény.
# # Írasd ki szbetuvelkezd.txt fájlba, egymás alá rendezve, az Sz-el kezdődő neveket.

lista = []

kategoriak = []

legfiatalabb = 0
legfiatalabbSzemely = ""

with open("ajandek.txt", "r", encoding="UTF8") as fajl:
        sorok = fajl.readlines()

        for sor in sorok[1:]:
            sor = sor.strip()
            sor = sor.split(";")

            nev = sor[0]
            termeknev =sor[1]
            ar = int(sor[2])
            szuletesi_ev = int(sor[3])
            kategoria = sor[4]

            lista.append([nev, termeknev, ar, szuletesi_ev, kategoria])

for item in lista:
    if item[3] > legfiatalabb:
         legfiatalabb = item[3]
         legfiatalabbSzemely = item[0]

    if item[4] not in kategoriak:
        kategoriak.append(item[4])

    akcios_ar = item[2] * (0.8)
    print(f"{item[0]} Eredeti ár: {item[2]} Ft | Akciós ár: {akcios_ar}")

print(f"Kategóriák száma: {len(kategoriak)}")
print(f"A legfiatalabb személy: {legfiatalabbSzemely}, {legfiatalabb}")

szbetus_nevek = []

for item in lista:
    if item[0].startswith("Sz"):
        szbetus_nevek.append(item[0])

with open("szbetuvelkezd.txt", "w", encoding="UTF8") as fajl:
    for nev in szbetus_nevek:
        fajl.write(nev + "\n")