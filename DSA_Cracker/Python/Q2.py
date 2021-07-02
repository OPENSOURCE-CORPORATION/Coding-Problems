# Find Max and Min of an Array

def Max_Min_1(Array):  # Time = O(n) , space = O(1)
    min = Array[0]
    max = Array[0]
    for i in range(len(Array)):
        if(min > Array[i]):
            min = Array[i]
        elif(max < Array[i]):
            max = Array[i]
    return max, min


def Max_Min_2(Array, start, end):  # Time = O(3n/2 -2) , Space=O(1)
    length = end - start + 1
    if (length == 1):
        Min = Array[start]
        Max = Array[start]
    elif (length == 2):
        Min = min(Array[start], Array[end])
        Max = max(Array[start], Array[end])
    else:
        mid = int((start+end)/2)
        max_left, min_left = Max_Min_2(Array, start, mid)
        max_right, min_right = Max_Min_2(Array, mid, end)
        Max = max(max_right, max_left)
        Min = min(min_right, min_left)
    return Max, Min


def Max_Min_3(Array, start, end):  # Time = O(n) , space = O(1)
    length = end - start+1
    if (length % 2 == 0):  # even
        Min = min(Array[0], Array[1])
        Max = max(Array[0], Array[1])
        steps = int((end-start)/2)
        x, y = 2, 3
        for i in range(steps):
            Min = min(Min, Array[x], Array[y])
            Max = max(Max, Array[x], Array[y])
            x += 2
            y += 2
    if(length % 2 != 0):
        Min = Array[0]
        Max = Array[0]
        steps = int((end-start)/2 + 0.5)
        x, y = 1, 2
        for i in range(steps):
            Min = min(Min, Array[x], Array[y])
            Max = max(Max, Array[x], Array[y])
            x += 2
            y += 2
    return Max, Min


Array = [1, 2, 3, 4, 5, 6, 3, 4, 5, 2, 4, 0, 3, 4, 8]
start = 0
end = len(Array)-1
Max, Min = Max_Min_3(Array, start, end)
print(f"Max is {Max} and Min is {Min}")
