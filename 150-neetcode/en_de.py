strs1 = ["lint","code","love","you"]
strs2 = "4#lint4#code4#love3#you"


def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s))+'#'+s
    return res


def decode(string):
    res, i = [], 0

    while i < int(len(string)):
        j = i
        while string[j] != '#':
            j+=1
        length = int(string[i:j])
        res.append(string[j+1:j+1+length])
        i =  j+1+length
    return res


print(encode(strs1))
print(decode(strs2))