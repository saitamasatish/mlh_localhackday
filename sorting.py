def insertionsort(l):
    """insertion sort function.

    parameter must be an integer list"""
    for i in range(1,len(l)):
       unsorted=l[i]
       while l[i-1]>unsorted and i>0:
           l[i-1],l[i]=l[i],l[i-1]
           i=i-1
    return l

print(insertionsort([2,3,5,1,8,9,0,7,5,6]))


               
