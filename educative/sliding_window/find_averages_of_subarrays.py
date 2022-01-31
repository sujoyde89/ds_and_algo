# for loop on range length
# add the element
# if the index is greater than equal to k-1 remove the starting element
# append the result

def find_averages_of_sub_arrays(k, arr):
    averages = []
    window_sum = 0
    for i in range(len(arr)):
        window_sum += arr[i]
        if i>=k-1:
            averages.append(window_sum/k)
            window_sum -= arr[i-k+1]
    return averages
            

def main():
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    result = find_averages_of_sub_arrays(k , arr)
    print("Averages of subarrays of size K: " + str(result))

main()