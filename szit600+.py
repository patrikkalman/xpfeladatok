betu = input("Kérem, adjon meg egy karaktert: ")
betu2 = input("Kérem, adjon meg egy másik karaktert: ")

if betu < betu2:
    print(f"A begepelt {betu} előrébb van az ábécében, mint {betu2}.")
elif betu > betu2:
    print( f" A begepelt {betu2} előrébb van az ábécében, mint {betu}.")
else:
    print("A két karakter azonos az ábécé sorrendjében.")
