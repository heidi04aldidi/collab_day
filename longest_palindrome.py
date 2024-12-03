def longest_palindrome_length(s):
    char_count = {}
    odd_count = 0

    for i in s:
        char_count[i] = s.count(i)

    if char_count[i]%2!=0:
        odd_count+=1
    
    lst2 = list(char_count.values())
    even_lst = [i for i in lst2 if i%2==0]
    odd_lst = [i for i in lst2 if i%2!=0 and i>=3]

    odd_lst.sort()
    
    ans = sum(even_lst)+sum(odd_lst)-(len(odd_lst)-1)
    return ans

s=input()
print(longest_palindrome_length(s))