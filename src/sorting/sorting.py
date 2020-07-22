# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here

    place = 0

    left_pointer = right_pointer = 0

    while left_pointer < len(arrA) and  right_pointer < len(arrB):

        if arrA[left_pointer] < arrB[right_pointer]:

            merged_arr[place] = arrA[left_pointer]
            left_pointer +=1
            place +=1
        
        else:

            merged_arr[place] = arrB[right_pointer]
            right_pointer += 1
            place +=1
    
    if len(arrA[left_pointer:])>0:

        for i in arrA[left_pointer:]:
            merged_arr[place] = i
            place +=1

    if len(arrB[right_pointer:])>0:

        for j in arrB[right_pointer:]:
            merged_arr[place] = j
            place +=1

    
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

    if len(arr) > 1:

        mid = len(arr) // 2

        return merge(merge_sort(arr[:mid]),merge_sort(arr[mid:]))

    else:
        
        return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

if __name__ == "__main__":
    
    print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))