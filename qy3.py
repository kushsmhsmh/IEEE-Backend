sum = int(input("Enter target sum: "))
l = [1,2,3,4,5]
le = len(l)
li = []
for i in range (le):
    for j in range(i, le):
        if l[i] + l[j] == sum:
            li.append((l[i], l[j]))
            
print(li)