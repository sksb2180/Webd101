c = int(input())
d = []
for i in range(c):
    b = int(input())
    for j in range(b):
        j = list(map(int,input().rstrip().split()))
        d.append(j)
    a = [subd for subd in d if subd[0] != 9 and subd[0] != 10 and subd[0] != 11]
    a.sort()
    print(a)
    if len(a)==0:
        print("0")
    else:
        b, c, d, e, f, g, h, i, j, y = ([] for i in range(10))

        for suba in a:
            if 1 in suba:
                b.append(a.index(suba))
            elif 2 in suba:
                c.append(a.index(suba))
            elif 3 in suba:
                d.append(a.index(suba))
            elif 4 in suba:
                e.append(a.index(suba))
            elif 5 in suba:
                f.append(a.index(suba))
            elif 6 in suba:
                g.append(a.index(suba))
            elif 7 in suba:
                h.append(a.index(suba))
            elif 8 in suba:
                i.append(a.index(suba))
        j.append(b)
        j.append(c)
        j.append(d)
        j.append(e)
        j.append(f)
        j.append(g)
        j.append(h)
        j.append(i)
        j = [i for i in j if i]
        for i in range(len(j)):
            x = j[i][-1]
            y.append(x)
        for i in range(1, len(y)):
            a[y[i]][1] = a[y[i - 1]][1] + a[y[i]][1]
        print(a[y[len(y) - 1]][1])










