# i, l, r
# for i
# for l
# i+l < r
# r-=1
#

def countTriplet(arr, n):
    # code here
    arr.sort()
    triplets = 0
    r = n-1
    if r<2:
        return triplets
    while r>=2:
        i=0
        l=r-1
        while i<l:
            total = arr[i] + arr[l]
            if total>arr[r]:
                l-=1
            elif total<arr[r]:
                i+=1
            else:
                triplets+=1
                i+=1
                l-=1
        r-=1
    return triplets
    
arr, n = [1, 5, 3, 2], 4
print (countTriplet(arr, n))