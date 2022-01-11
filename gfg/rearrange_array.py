def rearrange(arr, n): 
    ##Your code here
    r = n-1
    sub_elems = []
    for i in range(n):
        if i%2==0:
            sub_elems.append(arr[i])
            arr[i] = arr[r]
            r-=1
        else:
            sub_elems.append(arr[i])
            arr[i] = sub_elems[0]
            sub_elems.pop(0)
        print (i, arr, sub_elems)
    print (arr)

arr, n = [1, 2, 3, 4, 5, 6, 7, 8], 8
rearrange(arr, n)