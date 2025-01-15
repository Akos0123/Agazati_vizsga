# 1.Feladat
# Kérj be egy szót a felhasználótól, és vizsgáld meg, hogy valamelyik szóban van-e s vagy c.

szo = input("Adj meg egy szót: ")

if "s" in szo and "c" in szo:
    print("A szóban van c és s betű is.")
elif "s" in szo:
    print("A szóban s betű van")
elif "c" in szo:
    print("A szóban c betű van")
else:
    print("A szóban egyik betű sem szerepel.")
