x=9
mark=[]
while (x<9) and p
    p1 = input("enter X")
    mark.append(p1)
    count += 1
    p2 = input("enter O")
    while(p1==p2)
        p2 = input("space is full, enter 0 in a new location")
        if (p1 != p2)
            mark.append(p2)
            count += 1


