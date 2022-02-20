import math

def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    smallest_diff = math.inf
    for i in range(len(arr)-2):
        l = i+1
        r = len(arr)-1
        while l<r:
            target_diff = target_sum - arr[i] - arr[l] - arr[r]
            if target_diff == 0:
                return target_sum
            if abs(target_diff) < abs(smallest_diff):
                smallest_diff = target_diff
            if target_diff > 0:
                l+=1
            else:
                r-=1

    return target_sum - smallest_diff

def main():
  print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
  print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
  print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()