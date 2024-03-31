a = 1
b = 7

for i in range (1,8):
    for j in range (1,8):
        if j == a or j == b :
            print ("1", end = " ")
        else :
            print ("+", end =" ")
    a += 1
    b -= 1
    print ()

