def reverseWords(S):
    # code here 
    words = S.split('.')
    words = words[::-1]
    output = '.'.join(words)
    return output

S = 'I.dont.like.it'
print(reverseWords(S))
