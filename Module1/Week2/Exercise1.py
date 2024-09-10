def exerxise1(data, k):
    result = []
    l = 0
    while l + k <= len(data):
        result.append(max(data[l:l+k]))
        l += 1
    return result
test = [3,1,-2,-1,5,4]
print(exerxise1(test,2))


    