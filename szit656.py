karakterlanc = input("Kérem, adjon meg egy karakterláncot: ")
maganhangzokszama = sum(1 for karakter in karakterlanc if karakter.lower() in 'aeiou')
print(f"A karakterláncban {maganhangzokszama} magánhangzó található.")
