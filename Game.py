import random
print("Zagrajmy w gre!")
zgaduj = input("Zgadnij jaką liczbę z przedziału od 1 do 10 wybiorę: ")
zgaduj = int(zgaduj)
liczba = random.randint(1,10)
if zgaduj == liczba:
    print(f"Brawo zgadłeś/aś! Ta liczba to: {liczba}")
else:
    print(f"Nie zgadłeś/aś :(. Ta liczba to: {liczba}")
    