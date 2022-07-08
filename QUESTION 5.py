# QUESTION 5

def hyphen_sort(str):
    list_words=str.split('-')       # Creating list of words separated by '-'
    list_words.sort()               
    print('-'.join(list_words))     # Joining sorted list

# Driver Code
string=input()
hyphen_sort(string)