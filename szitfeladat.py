karakter = input("Kérem, adjon meg egy karaktert: ")

if karakter < 'n':
    print(f"A '{karakter}' karakter az 'n' karakter előtt van az ábécében.")
elif karakter > 'n':
    print(f"A '{karakter}' karakter az 'n' karakter után van az ábécében.")
else:
    print("A megadott karakter az 'n' karakterrel azonos az ábécé sorrendjében.")
