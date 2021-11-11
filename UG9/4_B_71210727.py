print("=====GEBYAR DISKON=====")
print("=====MASUKAN JUMLAH BARANG YANG DIPESAN=====")

a = int(input("KIPAS ANGIN DISKON 10% Rp 25.000,00 : "))
b = int(input("SEPEDA DISKON      55% Rp 6.000,00  : "))
c = int(input("HELM ROSSI DISKON  77% Rp 8.000,00  : "))

print("=====TOTAL=====")
print("TOTAL KIPAS ANGIN  : ",(10/100 * 25000) * a)
print("TOTAL SEPEDA SUPER : ",(55/100 * 6000) * b)
print("TOTAL SEPEDA MOTOR : ",(77/100 * 8000) * c)

diskona = (25000 * a) * 10/100
diskonb = (6000 * b) * 55/100
diskonc = (8000 * c) * 77/100

print("Jumlah total diskon yang didapat adalah Rp ", (diskona + diskonb + diskonc))
