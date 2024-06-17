sour = "halo"
tar = "hello"
def edit_distance(sour, tar):
    distance = [[0]*(len(tar)+1) for i in range(len(sour)+1)]
    for ti in range(len(tar)+1):
        distance[0][ti] = ti
    for tj in range(len(sour)+1):
        distance[tj][0] = tj
    del_cost = 0
    ins_cost = 0
    sub_cost = 0
    for i in range(1, len(sour)+1):
        for j in range(1, len(tar)+1):
            if sour[i - 1] == tar[j-1]:
                distance[i][j] = distance[i - 1][j - 1]
            else:
                del_cost = distance[i-1][j]
                ins_cost = distance[i][j-1]
                sub_cost = distance[i-1][j-1]
                
                if (del_cost<= ins_cost) and (del_cost<= sub_cost):
                    distance[i][j] = del_cost + 1
                elif (ins_cost<= del_cost) and (ins_cost<= sub_cost):
                    distance[i][j] = ins_cost + 1
                else:
                    distance[i][j] = sub_cost + 1
    print(distance)
    return distance[len(sour)][len(tar)]
print(edit_distance(sour,tar))