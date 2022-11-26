from itertools import combinations

def sub_set_sum(my_array, sub_set_sum):
   sub_array=[]
   for i in range(len(my_array)):
      for my_sub_set in combinations(my_array, i):

         if sum(my_sub_set) == sub_set_sum:
            sub_array.append(my_sub_set)
            print(my_sub_set)
   return sub_array

my_list = [59, 31, 39, 30, 35, 108, 113, 135, 44, 48, 124, 55, 30, 48, 74, 71, 113, 74, 74, 26, 26, 122, 92, 113, 43, 23, 43, 74, 74, 39, 39, 39, 39, 113, 31]
subset_sum = 53
print( sum(my_list)/3)
print(sub_set_sum( my_list, sum(my_list)/3))