def equilibriumPoint(A, N):
        # Your code here
        l = 0
        r = N-1
        left = A[l]
        right = A[r]
        while l<r:
            if left==right and ((r==l+2) or (r==l+1)):
                if r==l+2:
                    return l+2
                else:
                    l+=1
                    r-=1
                    left += A[l]
                    right += A[r]
            elif left<right:
                l += 1
                left += A[l]
            else:
                r -= 1
                right += A[r]
        return -1

A = '1 3 5 2 2'
A = [int(a) for a in A.split()]
N = len(A)
print (equilibriumPoint(A, N))