#flatten

def flat(arr):
    result=[]
    for i in arr:
        if type(i) is list:
            result.extend(flat(i))
        else:
            result.append(i)
    return result

print(flat([1,2,[3,4],[[5]]]))
