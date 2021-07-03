# Problem Link :
# Excel-Sheet Link  :
# youtube Video Link :

# o(n^2) O(1)

def Two_No_Sum_1(Array_1, Target_sum):
    length = len(Array_1)
    for i in range(length):
        for j in range(length):
            if(Array_1[i]+Array_1[j] == Target_sum and i != j):
                return Array_1[i], Array_1[j]
    return 0, 0

# o(n) O(n)


def Two_No_Sum_2(Array_1, Target_sum):
    length = len(Array_1)
    Target = []
    for i in range(length):
        if(Array_1[i] in Target):
            return Array_1[i], (Target_sum - Array_1[i])
        else:
            Target.append(Target_sum-Array_1[i])
    return 0, 0

# o(nlog(n)) O(1)


def Two_No_Sum_3(Array_1, Target_sum):
    Left_Ptr = 0
    Right_Ptr = len(Array_1) - 1
    while Left_Ptr < Right_Ptr:
        Sum = Array_1[Left_Ptr] + Array_1[Right_Ptr]
        if (Sum == Target_sum):
            return[Array_1[Left_Ptr], Array_1[Right_Ptr]]
        elif (Sum < Target_sum):
            Left_Ptr += 1
        elif (Sum > Target_sum):
            Right_Ptr -= 1
    return 0, 0


Array_ip = [2, 5, 7, 10, 13, 17, 19]
Target = 20
a, b = Two_No_Sum_3(Array_ip, Target)
print(f"The value of i is {a} and j is : {b}  ")
