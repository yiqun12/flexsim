# flexsim
# flexsim competition

###### use brute force to get the optimized order model:
###### there are 35! different sequences in 35 surgical cases. 
###### 35! = 371993326789901217467999448150835200000000
###### which makes brute force test all cases in flexsim impossible.
###### so we decide to switch to greedy
###### 1st step is form a array of all expected surgical time. 
###### The code below will get this whole array of all expected surgical time：
###### [59, 31, 39, 30, 35, 108, 113, 135, 44, 48, 124, 55, 30, 48, 74, 71, 113, 74, 74, 26, 26, 122, 92, 113, 43, 23, 43, 74, 74, 39, 39, 39, 39, 113, 31]

```

import csv
import operator

from typing import List

# Gets all possible subsets of input_array which doesn't include element from skip_indices
def get_subsets(input_array, skip_indices=[]):
    print(1)  
    def get_incremental_subsets(index, subsets):   
        print(1)   
        new_subsets = []
        new_subsets.append([index])    
        for count in range(len(subsets)):
            print(1)  
            current_subset = subsets[count].copy()
            current_subset.append(index)
            if len(current_subset) == 1:
                new_subsets.append([current_subset])
            else:
                new_subsets.append(current_subset)

        return subsets + new_subsets
    
    subsets = []
    for count in range(len(input_array)):
        print(1)  
        if count not in skip_indices:
            print(1)  
            subsets = get_incremental_subsets(count, subsets)    
    return subsets

# Sum of a subset
def get_subset_sum(input_array, subset_indices):
    return sum(input_array[subset_index] for subset_index in subset_indices)

# Find partition input_array in two subsets such that each subset have sum equal to sum_value. 
# Subset exclude elements present in skip_indices
def partition_two(input_array, skip_indices, sum_value):
    input_array_sum = sum(input_array)
    print(1)  
    for index in skip_indices:
        input_array_sum = input_array_sum - input_array[index]
        print(1)  
    if input_array_sum != 2*sum_value:      
        print(1)    
        return None
    
    subsets = get_subsets(input_array, skip_indices)
    print(1)  
    for index in range(len(subsets)):
        print(1)  
        if get_subset_sum(input_array, subsets[index]) == sum_value:
            print(1)  
            return subsets[index]
    return None
 

def partition_three(input_array):    
    # Check if input_array sum is actually multiple of 3
    input_array_sum = sum(input_array)
    if input_array_sum%3 != 0:        
        return None    
    print(1)  
    target_sum = input_array_sum/3
    #Iterate over all subsets
    for subset in get_subsets(input_array):
        # Skip subsets where sum is not equal to target_sum
        if get_subset_sum(input_array, subset) != target_sum:      
            continue
        print(1)       
        # If subset with target_sum is found, try finding two subsets with target_sum in remaining array 
        subset_1 = partition_two(input_array, subset, target_sum)
        if  subset_1 != None:      
            return [subset,\
                    subset_1,\
                    list(set([index for index in range(len(input_array))]) - set(subset) - set(subset_1))]
    return None

  
Expected_Surgical_Time = []
with open('sample.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Expected_Surgical_Time.append(int(row['Expected_Surgical_Time']))
      
print(Expected_Surgical_Time)
```
###### 2nd step is to split the array into three equal sum of expected surgical time:
###### I use the code below to find all the subarray sequences that equals to the 747 (target sum = sum of array_expected_time/3)
###### and there is 53845 different sequences that has the same target sum 747. 
```
from itertools import combinations

def sub_set_sum(my_array, sub_set_sum):
   sub_array=[]
   for i in range(len(my_array)):
      for my_sub_set in combinations(my_array, i):

         if sum(my_sub_set) == sub_set_sum:
            a = list(my_sub_set)
            a.sort()
            if a not in sub_array:
                sub_array.append(a)
                print(a)
            
   return sub_array

my_list = [59, 31, 39, 30, 35, 108, 113, 135, 44, 48, 124, 55, 30, 48, 74, 71, 113, 74, 74, 26, 26, 122, 92, 113, 43, 23, 43, 74, 74, 39, 39, 39, 39, 113, 31]
subset_sum = 53
print( sum(my_list)/3)
array_ = sub_set_sum( my_list, sum(my_list)/3)
```
###### utilize the array of expected time to match all 53845 different subarray sequences that has the same target in order to find out all ways of 3 partition subarray sequence in the expected time array. and there are roughtly 100k ways.  
```
def check(b,my_list_):
    for element in b:
        if(element not in my_list_):#yes
            return False#false
        else:
            my_list_.remove(element)
    return True
def thirdlist(b1_,b2_):
    my_list_ = [59, 31, 39, 30, 35, 108, 113, 135, 44, 48, 124, 55, 30, 48, 74, 71, 113, 74, 74, 26, 26, 122, 92, 113, 43, 23, 43, 74, 74, 39, 39, 39, 39, 113, 31]
    for element in b1_:
        my_list_.remove(element)
    for element in b2_:
        my_list_.remove(element)
    return(my_list)
def double_check(array_equal):
    print(array_equal)
    ts3 = [*array_equal[0], *array_equal[1],*array_equal[2]]
    print(sorted(ts3))
    my_list_1 = [59, 31, 39, 30, 35, 108, 113, 135, 44, 48, 124, 55, 30, 48, 74, 71, 113, 74, 74, 26, 26, 122, 92, 113, 43, 23, 43, 74, 74, 39, 39, 39, 39, 113, 31]
    print(sorted(my_list_1)==sorted(ts3))
    print(sum(array_equal[0])==sum(array_equal[1])==sum(array_equal[2]))
global_yes = []
for b1 in range(len(b)):
     for b0 in range(b1,len(b)):
      my_list = [59, 31, 39, 30, 35, 108, 113, 135, 44, 48, 124, 55, 30, 48, 74, 71, 113, 74, 74, 26, 26, 122, 92, 113, 43, 23, 43, 74, 74, 39, 39, 39, 39, 113, 31]
      for element in b[b0]:
        my_list.remove(element)
      if(check(b[b1],my_list)):
        print(len(global_yes))
        b1_sort = sorted(b[b1])
        b0_sort = sorted(b[b0])
        b2_sort = sorted(thirdlist(b[b0],b[b1]))
        if(sorted([ b1_sort, b0_sort, b2_sort]) not in global_yes):
            global_yes.append(sorted([ b1_sort, b0_sort, b2_sort]))
       
```

###### since we have 100k ways of partitioning the expected time array in three. We need to eleminate the wrong sequences as much as possible 
###### next step: add objectives to eliminate the wrong sequences. 
###### objectives1: some surgery can only operate in operating room 1. these surgery must be in the same subarray of the sequences set.eleminate those do not containes all the operating room1 surgery.
###### objective2: better assigned the surgeon at a suitable time interval.
```
```
