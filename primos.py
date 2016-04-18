numbers = range(2, 1000)
primos = []
primos_base = [2,3,5,7, 11, 13, 17, 19, 23]
for n in numbers:
    fl_p = False
    for p in primos:
        if n % p == 0:
            fl_p = True
            break
    if fl_p == False:
        primos.append(n)
		
print primos
	