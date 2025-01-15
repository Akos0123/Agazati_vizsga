szavak = ["A", "nap", "ragyog", "az", "égen", "és", "a", "madarak", "vidáman", "csiripelnek", "a", "fákon", "amíg", "az", "emberek", "sétálnak", "a", "parkban", "és", "élvezik", "a", "szép", "időt", "tavasz", "tarka", "tulipánok", "tündökölnek"]

db = 0

while True:
    szok = input("Adj meg egy szót! ")
    if len(szok) > 3:
         
         szavak.append(szok)
         print(f"A listához adott szó: {szok}")
         break
    else:
         print("A szónak hosszabbnak kell lennie, mint 3 betű.")

for i in szavak: 
    if i.startswith("t"):
            db += 1
            
print(f"A listában {db} db t-vel kezdődő szó van.")

tbetus = []

tbetus.append(db)

print(f"A t-vel kezdődő szavak: {';'.join(map(str,tbetus))}")