

def binary(arr,st,end):
    print("Which value find enter: ")
    n=int(input())
    flag=0
    a=0
    value=0
    while(st<=end):
        mid=st+(end-st)//2
        if(arr[mid]==n):
            a=mid
            value=arr[mid]
            flag=1
            break
        elif(arr[mid]>n):
            end=mid
        else:
            st=mid
    if(flag==1):
        print("value is: ",value,"At index is: ",a)
    else:
        print("Value ",n," is not found here!")
        
            
arr=[1,10,15,17,28]
print(arr)
n=5
binary(arr,0,n-1)