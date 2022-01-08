def quick_sort(arr, left, right):
    if left < right:
        # Partition the array by setting the position of the pivot value
        position = Partition(arr, left, right)
        # Sort the left
        quick_sort(arr, left, position - 1)
        print(arr,"left")
        # Sort the right
        quick_sort(arr, position + 1, right)
        print(arr,"right")

def Partition(arr, left, right):
    # set a pivot value as a point of reference
    pivot = arr[right]
    # create a variable to track the largest index of numbers lower than the  pivot
    low = left - 1
    for i in range(left,right):
        if arr[i] <= pivot:
            low += 1
            Swap(arr, i, low)
        else:
            print("marco")
     # place the value of the pivot location in the middle.
     # all numbers smaller than the pivot are on the left, larger on the right.
    Swap(arr, right, low + 1)
    # return the pivot index point
    return low + 1

def Swap(arr, i, low):
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp

if __name__ == "__main__":
    lst = [4,4,4,4,4,8,1,6,7,3,8,8]
    quick_sort(lst,0,len(lst)-1)


