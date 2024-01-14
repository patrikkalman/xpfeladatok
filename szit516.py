sorok_szama = 5

for i in range(sorok_szama, 0, -1):
    print("  " * (sorok_szama - i), end="")
    print("@ " * (2*i - 1))
