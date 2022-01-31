# left index and right index
# add values 
# if sum is less than target increase l
# if sum is more than target decrease r

def pair_with_targetsum(arr, k):
    l = 0
    r = len(arr)-1
    while l<r:
        sum_l_r = arr[l] + arr[r]
        if sum_l_r == k:
            return [l, r]
        elif sum_l_r<k:
            l+=1
        else:
            r-=1

def main():
  print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
  print(pair_with_targetsum([2, 5, 9, 11], 11))

main()
