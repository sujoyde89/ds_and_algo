# non duplicate index 1
# i = 1
# increment i
# if duplicate do nothing increment i but dont do anything with non duplicate index
# if non duplicate replace element of index with non duplicate

def remove_duplicates(arr):
    i = 1
    next_non_duplicate_index = 1
    while i<len(arr):
        if arr[i]!=arr[next_non_duplicate_index-1]:
            arr[next_non_duplicate_index] = arr[i]
            next_non_duplicate_index+=1
        i+=1
    return next_non_duplicate_index


def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))


main()