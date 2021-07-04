# Problem Link : Check Sheet link below
# Excel-Sheet Link  : https://drive.google.com/file/d/1L3EOLDMs-Fx2XoKclkCg1OVymDGh6psP/view?usp=sharing
# youtube Video Link :

# Q> Sort elements of an array which are 0,1,2 only without any sorting algo

def sort_without_sort_1(Array):  # Time :O(n) , Space : O(1)
    cnt_0 = 0
    cnt_1 = 0
    cnt_2 = 0
    for i in range(len(Array)+1):
        if(Array[i] == 0):
            cnt_0 += 1
        elif(Array[i] == 1):
            cnt_1 += 1
        else:
            cnt_2 += 1
    for i in range(len(Array)):
        if(cnt_0 != 0):
            Array[i] = 0
            cnt_0 -= 1
        elif(cnt_1 != 0):
            Array[i] = 1
            cnt_1 -= 1
        else:
            Array[i] = 2
    return Array


def sort_without_sort_2(Array):  # Time : O(n) , Space : O(1)
    pointer_0 = 0
    pointer_main = 0
    pointer_2 = len(Array) - 1s
    for i in range(len(Array)):
        if (Array[pointer_main] == 0):
            Array[pointer_0], Array[pointer_main] = Array[pointer_main], Array[pointer_0]
            pointer_main += 1
            pointer_0 += 1
            print("Switched 0,x")
        elif (Array[pointer_main] == 1):
            pointer_main += 1
        else:
            print("Switch 2 : x")
            Array[pointer_main], Array[pointer_2] = Array[pointer_2], Array[pointer_main]
            pointer_2 -= 1
    return Array

# 0,1,2,2,1,0,1,0,2,1,0,2,1


Array = [0, 1, 2, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 1, 2, 1, 0, 2, 1]
Output = sort_without_sort_2(Array)
print(Output)

# This Code is Written by Eshan Chawla aka The "Dead_Coder"
