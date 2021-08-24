# Problem Link : Check Sheet link below
# Excel-Sheet Link  : https://drive.google.com/file/d/1L3EOLDMs-Fx2XoKclkCg1OVymDGh6psP/view?usp=sharing
# Youtube Video Link :

# Q> Cylically Rotate elements by 1 Position
# Input :  1 2 3 4 5 6 7
# Output : 7 1 2 3 4 5 6

def Rotate(Array):  # Time : O(n) , Space : O(1)
    length = len(Array)
    temp = Array[length-1]
    for i in range(length-1, 0, -1):
        Array[i] = Array[i-1]
    Array[0] = temp
    return Array


def Rotate_2(Array):  # Time : O(n) , Space : O(1)
    length = len(Array)
    i = 0
    j = 1
    while(j <= length - 1):
        Array[i], Array[j] = Array[j], Array[i]
        j += 1
    return Array


Input = [1, 2, 3, 4, 5, 6, 7, 8]
Output = Rotate_2(Input)
print(Output)

# This Code is Written by Eshan Chawla aka The "Dead_Coder"
