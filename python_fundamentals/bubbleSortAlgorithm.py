arr=[1,5,3,2,0,8]

def bubbleSort(arr):
    for i in range(len(arr)-1):
        # print("\n","*"*80,"\nindex",i,"value",arr[i])
        print("\n","*"*80,"\nComparing",arr[i],arr[i+1])
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            print("swapped",arr[i],arr[i+1])
            print("array is now :",arr)
        else:
            print("no need to swap",arr[i],arr[i+1])

bubbleSort(arr)