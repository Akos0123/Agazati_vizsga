list = []
with open("termekek.txt ","r",encoding="utf-8")as file:
    sorok = file.readlines()
    for i in sorok[1:]:
        i = i.strip()
        i = i.split(";")
        termek = i[0]
        ar = int (i[1])
        eladott_mennyiseg = int(i[2])
        ev = int(i[3])
        list.append([termek,ar,eladott_mennyiseg,ev])
    legdragabbar = 0
    legdragabbtermek = ""

    darab = 0
    atlag = []
    for a in list:
        atlag.append(a[2])
        if a[0].startswith("C"):
            darab += 1
        
        
        if a[1]>legdragabbar:
            legdragabbar = a[1]
            legdragabbtermek = a[0]
        
    print(f"A legdrágább termék:{legdragabbar}, ({legdragabbtermek})")
    print(f"eladott mennyiség átlaga:{round(sum(atlag)/len(atlag))}")
    print(f"ennyi C betűs termék van: {darab}")
    
with open("c_betus_termekek.txt ","w",encoding="utf-8")as fajl:
    for ir in list:
         if ir[0].startswith("C"):
             fajl.write (f"{ir[0]}, {ir[1]}, {ir[2]}, {ir[3]}")
             print(f"{ir[0]}, {ir[1]}, {ir[2]}, {ir[3]}")
             
        # print(f"{a[0]},{a[1]}, {a[2]}, {a[3]}")
        



        








