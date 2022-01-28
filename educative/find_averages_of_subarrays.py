def find_averages_of_sub_arrays(k, arr):
    l=0
    averages = []
    window_sum = 0
    for i in range(len(arr)):
        window_sum += arr[i]
        if i>=k-1:
            averages.append(window_sum/k)
            window_sum -= arr[i-k+1]
    return averages
            


def main():
  result = find_averages_of_sub_arrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))

main()