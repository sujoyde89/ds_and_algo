def max_sub_array_of_size_k(k, arr):
    window_sum = 0
    max_window_sum = 0
    for i in range(len(arr)):
        window_sum += arr[i]
        if i>=k-1:
            max_window_sum = max(max_window_sum, window_sum)
            window_sum -= arr[i-k+1]
    return max_window_sum

def main():
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    result = max_sub_array_of_size_k(k, arr)
    print("Averages of subarrays of size K: " + str(result))

main()