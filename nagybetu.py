nagybetu = input("Kérem, adjon meg egy nagybetűt: ")

if 'A' <= nagybetu <= 'Z':
    kisbetusALAK = ord(nagybetu) + ord('a') - ord('A')
    kisbetu = chr(kisbetusALAK)
    print(f"A kisbetűs változat: {kisbetu}")
else:
    print("Hibás bemenet! Kérlek, adj meg egy nagybetűt.")
