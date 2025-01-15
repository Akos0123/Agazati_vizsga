konyvek = []

with open("konyvek.txt", "r", encoding="UTF8") as file:
    sorok = file.readlines()

    for sor in sorok[1:]:
        sor = sor.strip()
        sor = sor.split(";")

        cim = sor[0]
        ar = int(sor[1])
        eladott = int(sor[2])
        ev = int(sor[3])

        konyvek.append([cim, ar, eladott, ev])

print("2010 után kiadott könyvek:")
for konyv in konyvek:
    if konyv[3] > 2010:
        print(f"{konyv[0]}, {konyv[1]}, {konyv[2]}, {konyv[3]}")

legolcsobb_konyv = konyvek[0]
for konyv in konyvek:
    if konyv[1] < legolcsobb_konyv[1]:
        legolcsobb_konyv = konyv

print(f"A legolcsóbb könyv: {legolcsobb_konyv[0]} {legolcsobb_konyv[1]} Ft")

print("Harry Potter könyvek kiírva a fájlba:")
with open("HarryPotter_konyvek.txt", "w", encoding="UTF8") as fajl:
    for a in konyvek:
        if a[0].startswith("Harry Potter"):
            fajl.write(f"{a[0]}\n")
            print(f"{a[0]}")
