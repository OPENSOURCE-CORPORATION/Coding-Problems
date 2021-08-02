# Problem Link : Check Sheet link below
# Excel-Sheet Link  : https://drive.google.com/file/d/1L3EOLDMs-Fx2XoKclkCg1OVymDGh6psP/view?usp=sharing
# Youtube Video Link :

# Q> Find Union and Intersections of 2 Arrays

# Fundamental / Naive Approach
def Solution_1(Array_1, Array_2):  # Time: O(m*n), Space: O(0)
    Union = Array_1
    Intersection = []
    for i in range(len(Array_2)):
        if(Array_2[i] in Union):
            Intersection.append(Array_2[i])
        else:
            Union.append(Array_2[i])
    return Union, Intersection



# Time : O((m(log(m) + n(log(n)) + (m + n)) ,Space : O(1)
def Solution_2(Array_1, Array_2):
    Array_1.sort()
    Array_2.sort()
    # Array_1 will be shorter
    if(len(Array_1) > len(Array_2)):
        Array_1, Array_2 = Array_2, Array_1
    i = 0
    j = 0
    Union = []
    Intersection = []
    while(i <= len(Array_1)-1 and j <= len(Array_2)-1):
        if(Array_1[i] > Array_2[j]):
            Union.append(Array_2[j])
            j += 1
        elif(Array_1[i] < Array_2[j]):
            Union.append(Array_1[i])
            i += 1
        else:
            Union.append(Array_1[i])
            Intersection.append(Array_1[i])
            i += 1
            j += 1
    # temp = len(Array_1) - 3                                   # This is wrong do not do like at and repeat the mistake i did
    # for i in range(len(Array_2) - len(Array_1) + 3):
    #     Union.append(Array_2[temp])
    #     # print(Array_2[temp])
    #     temp += 1
    
    while(j < len(Array_2)):
        Union.append(Array_2[j])
        j += 1
    return Union, Intersection


Array_1 = [2, 1, 3, 4, 5, 6, 7]
Array_2 = [2, 5, 4, 9, 8, 7, 10, 11, 13, 45]
UNION, INTERSECTION = Solution_1(Array_1, Array_2)
UNION.sort()
print(f"The union of 2 Arrays is : {UNION}")
print(f"The intersections of 2 Arrays is : {INTERSECTION}")

# This Code is Written by Eshan Chawla aka The "Dead_Coder"
