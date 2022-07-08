# QUESTION 2

def palindrome(s):
    list_s = list(s)
    list_s.reverse()
    s_new = ''.join(list_s)
    ans = False
    if s_new == s:            # if new reversed string = original string then true
        ans = True
    return ans


# Driver Code
string = input()
print(palindrome(string))
