import math
from prime import primes
# import decimal # type: ignore
# decimal.getcontext().prec = 100


limit = 10**10
sols = set()
n = math.isqrt(limit)
sf = [i for i in range(n+1)]
p = primes(n)

def pells(D):
    if math.isqrt(D) ** 2 == D:
        return
    
    
    # d = decimal.Decimal.sqrt(decimal.Decimal(D))
    d = math.sqrt(D)

    x0 = math.floor(d)
    y0 = 1
    if x0**2 - D * y0**2 == 1:
        return x0, y0
    d -= math.floor(d)
    d = 1/d

    y1 = math.floor(d)
    x1 = y1*x0+1
    d -= math.floor(d)
    d = 1/d
    if x1**2 - D * y1**2 == 1:
        return x1, y1
    
    x = x1
    y = y1

    while x < limit:
        h = math.floor(d)

        x = h*x1 + x0
        y = h*y1 + y0
        if x**2 - D*y**2 == 1:
            return x, y
        
        x0 = x1
        y0 = y1
        x1 = x
        y1 = y

        d -= h
        d = 1/d


for i in p:
    q = i**2
    while q < n:
        for j in range(q, n+1, q):
            sf[j] = sf[j] // (i**2)
        q *= i**2



m = 1
while 2*m**2 + 2*m <= limit:
    c = 1

    # print("----")

    #base solution
    k = 2*m**2 + m
    d = 1
    a, b = pells(sf[m] * sf[m+1])
    # a = 2*m + 1
    # b = 2

    x = 2*(m+1)*k + (m*(m+1))
    y = 2*(k+d+m) + m-1
    t = math.isqrt((m*(m+1)) // (sf[m] * sf[m+1]))
    y = y * t
    sols.add(k+m)
    # print(m, k+m, x, y, "WORKS")

    # print(a, b)

    while k + m <= limit and a and b:
        # sols.add(k+m) 
        nx = a*x + sf[m] * sf[m+1]*b*y
        ny = x*b + a*y
        x = nx
        y = ny
        k = (x - (m*(m+1)))//(2*(m+1))
        # print(m, k+m, x, y)
        if (x - (m*(m+1))) % (2*(m+1)) == 0 and k+m <= limit and (y//t - (m-1))%2 == 0:
            # print(m, k+m, x, y, "WORKS", (y // t - (m-1)))
            c += 1
            sols.add(k+m)

    m += 1
    # print(c)

# print(sols)
print(sum(sols))
# print(sols)
    

"""
1 4 14 10
1 21 82 58
1 120 478 338
1 697 2786 1970
1 4060 16238 11482
1 23661 94642 66922
6
2 12 66 27
2 110 654 267
2 1080 6474 2643
2 10682 64086 26163
4
3 24 180 52
3 315 2508 724
3 4368 34932 10084
3 60819 486540 140452
4
4 40 380 85
4 684 6820 1525
4 12240 122380 27365
3
5 60 690 126
5 1265 15150 2766
5 27720 332610 60726
3
6 84 1134 175
6 2106 29442 4543
6 54600 764358 117943
3
7 112 1736 232
7 3255 52024 6952
7 97440 1558984 208328
3
8 144 2520 297
8 820 14688 1731
8 4760 85608 10089
8 27724 498960 58803
4
9 180 3510 370
9 6669 133290 14050
2
10 220 4730 451
10 9030 198550 18931
2
11 264 6204 540
11 11891 285252 24828
2
12 312 7956 637
12 15300 397644 31837
2
13 364 10010 742
13 19305 540358 40054
2
14 420 12390 855
14 23954 718410 49575
2
15 480 15120 976
15 29295 937200 60496
2
16 544 18224 1105
16 35376 1202512 72913
2
17 612 21726 1242
17 42245 1520514 86922
2
18 684 25650 1387
18 49950 1897758 102619
2
19 760 30020 1540
19 58539 2341180 120100
2
20 840 34860 1701
20 68060 2858100 139461
2
21 924 40194 1870
21 78561 3456222 160798
2
22 1012 46046 2047
22 90090 4143634 184207
2
23 1104 52440 2232
1
24 1200 59400 2425
24 11772 588000 24005
2
25 1300 66950 2626
1
26 1404 75114 2835
1
27 1512 83916 3052
1
28 1624 93380 3277
1
29 1740 103530 3510
1
30 1860 114390 3751
1
31 1984 125984 4000
1
32 2112 138336 4257
1
33 2244 151470 4522
1
34 2380 165410 4795
1
35 2520 180180 5076
1
36 2664 195804 5365
1
37 2812 212306 5662
1
38 2964 229710 5967
1
39 3120 248040 6280
1
40 3280 267320 6601
1
41 3444 287574 6930
1
42 3612 308826 7267
1
43 3784 331100 7612
1
44 3960 354420 7965
1
45 4140 378810 8326
1
46 4324 404294 8695
1
47 4512 430896 9072
1
48 4704 458640 9457
48 65208 6388032 131719
2
49 4900 487550 9850
49 28441 2841650 57410
2"""