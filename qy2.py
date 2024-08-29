n = int(input("Enter n: "))
arr = [[0] * n for _ in range(n)]
count = 1
rs = 0
re = n-1
cs=0
ce=n-1
c=0
r= 0
cc = 0
cr = 0
for i in range(0, n**2):
    arr[r][c] = count
    if r == rs and c == cs:
        rc = 0
        cc = 1
        if ((r-c) != 0):
            cs+=1
            ce-=1
            re-=1
    elif r == rs and c == ce:
        rc = 1
        cc = 0
    elif r == re and c == ce:
        rc = 0
        cc = -1
    elif r == re and c == cs:
        rc = -1
        cc = 0
        rs += 1
    r+=rc
    c+=cc
    count +=1

for i in range(0, n):
     for j in range (0, n):
         print(arr[i][j], "\t", end = '')
     print()
    