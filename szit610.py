elsosor = input("Kérem, adjon meg egy első karaktersorozatot: ")
masodiksor = input("Kérem, adjon meg egy második karaktersorozatot: ")

if len(elsosor) > len(masodiksor):
    print(f"Az első karaktersorozat hosszabb, {elsosor}")
elif len(elsosor) < len(masodiksor):
    print(f"A második karaktersorozat hosszabb, {masodiksor}")
else:
    print("A két karaktersorozat egyenlő hosszú.")
