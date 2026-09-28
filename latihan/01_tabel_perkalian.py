# Program Tabel Perkalian
# Input: bilangan bulat n
# Proses: mengulang perkalian n dari 1 sampai 10
# Output: tabel perkalian n

n = int(input("Bilangan: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")