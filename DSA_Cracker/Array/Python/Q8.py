# Problem Link : Check Sheet link below
# Excel-Sheet Link  : https://drive.google.com/file/d/1L3EOLDMs-Fx2XoKclkCg1OVymDGh6psP/view?usp=sharing
# Youtube Video Link :

# Q> contiguous sub-array with maximum sum AKA the KADANES Algorithm

def Max_Subarray(Array):  # Time : O(n^2) , Space : O(1)
    Max_Sum = Array[0]
    for i in range(0, len(Array)):
        for j in range(i, len(Array)):
            sub_array_sum = 0
            temp_i = i
            for k in range(j-i + 1):
                sub_array_sum += Array[temp_i]
                temp_i += 1
            Max_Sum = max(sub_array_sum, Max_Sum)
    return Max_Sum


def kadanes(Array):  # Time : O(n) , Space : O(1)
    Max_sum = Array[0]
    Current_sum = Array[0]
    lenght = len(Array)
    i = 1
    while (lenght > i):
        Current_sum += Array[i]
        if(Current_sum < 0):
            Current_sum = 0
        if(Current_sum > 0):
            Max_sum = max(Max_sum, Current_sum)
    return Max_sum


Array = [1, 2, 3, -2, 5]
Solution = kadanes(Array)
print(f"Max Subarray : {Solution}")
# This Code is Written by Eshan Chawla aka The "Dead_Coder"
