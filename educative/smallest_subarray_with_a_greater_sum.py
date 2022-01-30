# start a left index
# start a right index
# increase the right index till subarray sum is less than k
# increase the left index till subarray sum is more than k

import math

def smallest_subarray_with_a_greater_sum(k, arr):
    l = 0
    subarray_sum = 0
    smallest_subarray = math.inf
    for r in range(len(arr)):
        subarray_sum += arr[r]
        while subarray_sum>=k:
            smallest_subarray = min(smallest_subarray, r-l+1)
            subarray_sum -= arr[l]
            l+=1
    return 0 if smallest_subarray == math.inf else smallest_subarray

def main():
    arr = [2, 1, 5, 2, 3, 2]
    k = 7
    result = smallest_subarray_with_a_greater_sum(k , arr)
    print(result)

main()