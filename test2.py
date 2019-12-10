def divisors(m):
    x = []
    i = 1
    while i <= m:
        if (m % i==0) :
            x.append(i)
        i=i+1

    return x

def intset(arr1, arr2, arr3):
    s1 = set(arr1)
    s2 = set(arr2)
    s3 = set(arr3)

    set1 = s1.intersection(s2)
    result_set = set1.intersection(s3)
    final_set = list(result_set)
    return final_set



start = 1
end = 10000
lst1 = []
for val in range(start, end + 1):
    if val > 1:
        for n in range(2, val):
            if (val % n) == 0:
                break
        else:
            val
            lst1.append(val)


lst2 = []
lst3 = []
a = int(input())
for i in range(a):
    x, y = [int(x) for x in input().split()]
    print(divisors(x))
    print(divisors(y))
    print(lst1)
    lst2 = divisors(x)
    lst3 = divisors(y)
    c = intset(lst1, lst2, lst3)
    print(c)
    if len(c)==0:
        print("No")
    elif len(c)==1 and c[0]==1:
        print("No")
    else:
        print("Yes")
