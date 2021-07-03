# Problem Link : Check Sheet link below
# Excel-Sheet Link  : https://drive.google.com/file/d/1L3EOLDMs-Fx2XoKclkCg1OVymDGh6psP/view?usp=sharing
# youtube Video Link :

# Q> Find the Kth Maximum and Minimum Element of the Given Input Array

def Solution(Array, k):    # Time : O(long(n)) Space = O(1)
    length = len(Array)
    if(length < k):
        return -1, -1
    else:
        Array = sorted(Array)
        return(Array[length-k], Array[k-1])


Array = [1, 2, 34, 5, 6, 5, 7, 6, 7, 65, 67]
k = 2

K_Max, K_Min = Solution(Array, k)
print(K_Max, K_Min)

# This Code is Written by Eshan Chawla aka The "Dead_Coder"
