def search_triplets(arr):
    arr.sort()
    outputs = []
    for i in range(len(arr)-2):
        l = i+1
        r = len(arr)-1
        while l<r:
            total = arr[i] + arr[l] + arr[r]
            if total==0:
                outputs.append([arr[i], arr[l], arr[r]])
                l+=1
                r-=1
                while l<r and arr[l]==arr[l-1]:
                    l+=1
                while l<r and arr[r]==arr[r+1]:
                    r-=1
            elif total<0:
                l+=1
            else:
                r-=1
    return outputs



def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(search_triplets([-5, 2, -1, -2, 3]))

main()