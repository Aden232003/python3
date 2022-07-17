def duplicate_encode(word):
    word = word.lower()
    char = list(word)
    ans = [0]*len(word)
    ansStr = ""
    
    for i in range(len(char)-1):
        for j in range(len(char)):
            if j>i and char[i]==char[j]:
                ans[i]=')'
                ans[j]=')'
    for k in range(len(char)):
        if ans[k]!=')':
            ans[k]='('
    for i in ans:
        ansStr+=i
    return ansStr

str1 = 'recede'
print(duplicate_encode(str1))