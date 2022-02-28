def max_contiguous_array(arr):
    max_ending_here = 0
    max_so_far = 0
    for i in arr:
         max_enging_here = max_ending_here + i
         max_ending_here = max(max_ending_here, i)
         max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

if __name__ == '__main__':
 
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
 
    print("The sum of contiguous sublist with the largest sum is", max_contiguous_array(A))