def bubblesort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j]>=a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
x=[1,78,90,67,89]
print("before sorting",x)
bubblesort(x)
print("after sorting",x)
            
