def insertion_sort(list_to_sort):
    for i in range(1,len(list_to_sort)):

        j = i - 1
        temp = list_to_sort[i]

        while j>=0 and temp < list_to_sort[j]:
            list_to_sort[j + 1] = list_to_sort[j]
            j -= 1

        list_to_sort[j+1] = temp
