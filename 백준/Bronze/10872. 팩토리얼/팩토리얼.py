def fac_1(x):
    anw = 1
    for i in range(1, x+1):
        anw = anw * i
    print(anw)

N = int(input())
fac_1(N)
