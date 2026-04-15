# 1
royxat = [12, 3, 45, 7, 18, 2]
kichik_10 = [i for i in royxat if i < 10]
print(kichik_10)


# 2
royxat = [5, 10, 15, 20, 25]
beshga_bolinadi = [i for i in royxat if i % 5 == 0]
print(beshga_bolinadi)


# 3
royxat = [-10, -5, 0, 5, 10]
musbat_va_nol = [i for i in royxat if i >= 0]
print(musbat_va_nol)


# 4
royxat = [1, 2, 3, 4, 5, 6]
toq_kvadrat = [i**2 for i in royxat if i % 2 != 0]
print(toq_kvadrat)


# 5
royxat = [9, 16, 25, 36, 49]
ildiz = [i**0.5 for i in royxat]
print(ildiz)
