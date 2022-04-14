from collections import Counter

""" if current number is 1 + previous number then no count for number cur-1 ans curr+1 """

def delete_to_Earn(arr):
    look_up = Counter(arr)
    print(look_up)
    point1, point2 = 0, 0   # point2 is the most recent cumulative point
    # keep making point2 the max possible to earn in the available array
    for i in range(len(list(look_up.keys()))):
        cur_point = arr[i] * look_up[arr[i]]
        #  decide on all cases based on the rule......TODO
        if (i > 0 and i < (len(arr)-1)) and (arr[i] == arr[i-1]+1 or arr[i+1]-1 == arr[i] or arr[i-1] == arr[i]):
            temp = point2
            point2 = max(cur_point + point1, point2)
            point1 = temp
        elif (i == (len(arr)-1)) and (arr[i-1]+1 == arr[i] and arr[i-1] == arr[i]):
            temp = point2
            point2 = max(cur_point + point1, point2)
            point1 = temp
        else:
            temp = point2
            point2 = cur_point + point2
            point1 = temp
    return point2


print(delete_to_Earn([3,4,2,2,5,7]))
