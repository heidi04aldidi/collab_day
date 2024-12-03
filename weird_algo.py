def weird_algo(n):
    if n==1:
        return 1
    else:
        if n%2==0:
            print(n, end=" ")
            new_n = int(n/2)
            return weird_algo(new_n)
        else:
            print(n, end=" ")
            new_n = n*3+1
            return weird_algo(new_n)

n = int(input())
print(weird_algo(n))