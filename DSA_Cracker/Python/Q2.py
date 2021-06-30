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


def Max_Min_2(Array):
    size = len(Array)
    if(size == 1):
        Max = Array[0]
        Min = Array[0]
    elif(size=2):
        if(Array[0] > Array[1]):
            Max = Array[0]
            Min = Array[1]
        else:
            Max = Array[1]
            Min = Array[0]
    else:
        Mid = int(size/2)
        left_Array = Array(0
                           Mid)

    # Sample Commit


Array = [1, 2, 3, 4, 5, 6, 3, 4, 5, 2, 4, 0, 3, 8]
start = 0
end = len(Array)-1
Max, Min = Max_Min_1(Array)
print(f"Max is {Max} and Min is {Min}")
