
def binary_search_iterative(arr, elem):
    start = 0
    end = len(arr)
    step = 1
    while start<=end:
        mid = (start + end)//2
        print("Subarray in step {}: {}".format(step, str(array[start:end+1])))
        if elem==arr[mid]:
            return mid, step
        elif elem>arr[mid]:
            start = mid+1
        elif elem<arr[mid]:
            end = mid-1
        step+=1
    return -1, step

element = 18
array = [1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29]
ind, step = binary_search_iterative(array, element)
print(f'Index of {element}: {ind} found in step {step}')