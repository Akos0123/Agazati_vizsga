valuta = input("Milyen valutáról szeretne váltani?")
osszeg = float(input("Adja meg az átválandó összeget:"))

if valuta == "USD":
    print(f"Az átváltott összeg eredménye: {osszeg * 401} HUF")
elif valuta == "HUF":
    print(f"Az átváltott összeg eredménye: {osszeg / 401} USD")
else:
    print("Nincs ilyen valuta.")