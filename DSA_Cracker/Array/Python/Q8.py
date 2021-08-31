# Problem Link : Check Sheet link below
# Excel-Sheet Link  : https://drive.google.com/file/d/1L3EOLDMs-Fx2XoKclkCg1OVymDGh6psP/view?usp=sharing
# Youtube Video Link :

# Q> contiguous sub-array with maximum sum AKA the KADANES Algorithm

def Max_Subarray(Array):  # Time : O(n^2) , Space : O(1)
    Max_Sum = Array[0]
    for i in range(len(Array)):
        for j in range(i, len(Array)):
            sub_array_sum = 0
            # now to find the sum of the subarray at ends(i, j)
            for k in range(i, j+1):
                sub_array_sum += Array[k]
            Max_Sum = max(sub_array_sum, Max_Sum)
    return Max_Sum


def kadanes(Array):  # Time : O(n) , Space : O(1)
    Max_sum = Array[0]
    Current_sum = Array[0]
    length = len(Array)
    i = 1
    # while (length > i):
    for i in range(length):
        Current_sum += Array[i]
        if(Current_sum < 0):
            Current_sum = 0
        if(Current_sum > 0):
            Max_sum = max(Max_sum, Current_sum)
        # i += 1
    return Max_sum


Array = [1, -2, 3, 6, -5]
Solution = kadanes(Array)
print(f"Max Subarray Sum : {Solution}")
# This Code is Written by Eshan Chawla aka The "Dead_Coder"
