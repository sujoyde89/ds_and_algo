# unique_char dictionary with character:max index
# substring max
# left index
# for loop with a right index
# update unique char with max index
# if len unique_char == k, update substring max
# while unique char is greater than k, check if l==max index of char and add l

def longest_substring_with_k_distinct(str1, k):
    substring_max = 0
    unique_char = {}
    l = 0
    for r in range(len(str1)):
        char_str = str1[r]
        unique_char[char_str] = r
        if len(unique_char)==k:
            substring_max = max(r-l+1, substring_max)
        while len(unique_char)>k:
            if l==unique_char[char_str]:
                unique_char.pop(char_str)
            l+=1
    return substring_max

def main():
    str1 = 'araaci'
    k = 2
    result = longest_substring_with_k_distinct(str1, k)
    print(result)

main()