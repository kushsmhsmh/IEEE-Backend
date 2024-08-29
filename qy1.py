s1 = input("Enter string1: ")
s2 = input("Enter string2: ")
c = 0
for i in s1:
    if i in s2:
        print("Not complementary")
        c=0
        break
    else:
        c=1
        
if c == 1:
    print("Complementary")