def aser(arr,num,diff):
    n=len(arr)
    count=0
    for i in range(n):
        if(abs(arr[i]-num)<=diff):
            count+=1
    if count:
        return count
    return 0
arr=list(map(int,input().split()))
num=int(input())
diff=int(input())
print(aser(arr,num,diff))
