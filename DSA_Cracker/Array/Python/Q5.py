# Problem Link : Check Sheet link below
# Excel-Sheet Link  : https://drive.google.com/file/d/1L3EOLDMs-Fx2XoKclkCg1OVymDGh6psP/view?usp=sharing
# Youtube Video Link :

# Q> Move -ve no in the begining

def Solution(Array):  # Time : O(n) , Space : O(1)
    length = len(Array)
    where_to_replace = 0
    for main_pointer in range(length):
        if(Array[main_pointer] < 0):
            Array[where_to_replace], Array[main_pointer] = Array[main_pointer], Array[where_to_replace]
            where_to_replace += 1
    return Array


def Solution_2(Array):
    length = len(Array)
    where_to_replace = 0
    main_pointer = len(Array)-1
    while(where_to_replace < main_pointer):
        if(Array[main_pointer] < 0 and Array[where_to_replace] < 0):
            where_to_replace += 1
        elif(Array[main_pointer] < 0 and Array[where_to_replace] >= 0):
            Array[where_to_replace], Array[main_pointer] = Array[main_pointer], Array[where_to_replace]
            where_to_replace += 1
            main_pointer -= 1
        elif(Array[main_pointer] >= 0 and Array[where_to_replace] >= 0):
            main_pointer -= 1
        else:       # left pointer -ve , Right pointer is Positive
            where_to_replace += 1
            main_pointer -= 1

    return Array


Array = [-12, 11, -13, -5, 6, -7, 5, 3, -6]
Output = Solution_2(Array)
print(Output)
# This Code is Written by Eshan Chawla aka The "Dead_Coder"
