# Find Max and Min of an Array

def Max_Min_1(Array):  # Time : O(n)   , Space = O(1)
    Max = Array[0]
    Min = Array[0]
    for i in range(len(Array)):
        if(Max < Array[i]):
            Max = Array[i]
        elif(Min > Array[i]):
            Min = Array[i]
    return Max, Min


# def Max_Min_2(Array):


Array = [1, 2, 3, 4, 5, 6, 3, 4, 5, 2, 4, 0, 3, 8]
start = 0
end = len(Array)-1
Max, Min = Max_Min_1(Array)
print(f"Max is {Max} and min is {Min}")
