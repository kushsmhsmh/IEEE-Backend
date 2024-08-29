def gc(a, b):
    while(b):
        a, b = b, a % b
    return a
l=[]
for i in range(0, 5):
    a = int(input("Enter number: "))
    l.append(a)
    if i > 0:
        gcd = gc(l[i], l[(i-1)])

print(gcd)