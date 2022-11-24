###use brute force to get the optimized order model:
##there is 35! ways of 35 patients. 
##which is 371993326789901217467999448150835200000000
##use greedy.
###split array of 35 surgicl time intwo 3 similar/equal sum
###calculate the each order's time. 
##compare. 
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

'''

start_time = 0
end_time=0
PACU = { #true = avaliable false = not available 
  1: [True,start_time,end_time],
  2: [True,start_time,end_time],
  3: [True,start_time,end_time],
  4: [True,start_time,end_time],
  5: [True,start_time,end_time],
  6: [True,start_time,end_time],
  7: [True,start_time,end_time],
  8: [True,start_time,end_time],
  9: [True,start_time,end_time]
}
PreOp = { #true = avaliable false = not available 
  1: [True,start_time,end_time],
  2: [True,start_time,end_time],
  3: [True,start_time,end_time],
  4: [True,start_time,end_time]
}
OR = { #true = avaliable false = not available 
  1: [True,start_time,end_time],
  2: [True,start_time,end_time],
  3: [True,start_time,end_time],
}


'''