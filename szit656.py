karakterlanc = input("Kérem, adjon meg egy karakterláncot: ")

maganhangzokszama = 0

for karakter in karakterlanc:
    if karakter.lower() in 'aáeéiíoóöőuúüű':
        maganhangzokszama += 1

print(f"A karakterláncban {maganhangzokszama} magánhangzó található.")
