def checkpossibility(self,array:list[int])->bool:
    n,index=len(array),0
    if n==1:
        return True
    for i in range(1,n):
        if array[i] < array[i-1]:
            if index!=0:
                return False
            index=i
    if(index==0 or index==1 or index==n-1):
        return True
    if(array[index-1] > array[index+1] and array[index-2] > array[index]):
        return False

    return True
