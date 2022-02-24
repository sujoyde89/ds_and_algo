def square_sorted_array(arr):
    length = len(arr)
    output = [0 for i in range(length)]
    l = 0
    r = length-1
    ind = length-1
    while l<r:
        l2 = arr[l]**2
        r2 = arr[r]**2
        if l2<r2:
            output[ind] = r2
            r-=1
            ind-=1
        elif l2>=r2:
            output[ind] = l2
            l+=1
            ind-=1
    return output 

def main():

  print("Squares: " + str(square_sorted_array([-2, -1, 0, 2, 3])))
  print("Squares: " + str(square_sorted_array([-3, -1, 0, 1, 2])))


main()
        