# Problem Link : Check Sheet link below
# Excel-Sheet Link  : https://drive.google.com/file/d/1L3EOLDMs-Fx2XoKclkCg1OVymDGh6psP/view?usp=sharing
# Youtube Video Link :

# Q> Find The minimum no of Jumps to Reach the End of the Array

# User function Template for python3
class Solution:
    def minJumps(self, arr, n):

        Current_Block = 0
        Max_Range = arr[Current_Block]
        Max_Range_Value = arr[0]
        Max_Range_Block = 0
        Jump_Path = [0]
        reached = False
        while reached == False:
            for i in range(Max_Range):
                if(arr[i + Current_Block]+Current_Block > Max_Range_Value):
                    Max_Range_Block = i+Current_Block
                    Max_Range_Value = arr[Max_Range_Block]
            Jump_Path.append(Max_Range_Block)
            if(Max_Range_Value >= n):
                reached = True
                return len(Jump_Path) - 1
            elif(Max_Range_Value == 0):
                reached = True
                return 0
            else:
                Current_Block = Max_Range_Block
                Max_Range = arr[Current_Block]

        # code here


# 1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    # T = int(input())
    # for i in range(T):
    # 	n = int(input())
    # 	Arr = [int(x) for x in input().split()]
    # 	ob = Solution()
    n = 11
    Arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    ob = Solution()
    ans = ob.minJumps(Arr, n)
    print(ans)
# } Driver Code Ends

# This Code is Written by Eshan Chawla aka The "Dead_Coder"
