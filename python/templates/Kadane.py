# Kadane for max subarray
array = []
overall_max = float("-inf")
curr_sum = 0

i = 0
while i < len(array):
    curr_sum += array[i]
    
    overall_max = max(curr_sum, overall_max)
    if (curr_sum < 0):
        curr_sum = 0
    i+=1
print(overall_max)
