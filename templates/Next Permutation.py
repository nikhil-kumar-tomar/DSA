def permu(array):
    i = len(array) - 1
    while array[i-1] > array[i]:
        i-=1
    p = 0
    if i > 0:
        p = i-1

    temp_i = i
    mins = i
    while temp_i < len(array):
        if array[temp_i] < array[mins] and array[temp_i] > array[p]:
            mins = temp_i
        temp_i += 1

    array[p], array[mins] = array[mins], array[p]
  
    temp_arr = array[i:len(array)]
    temp_arr.sort()
    temp_arr = array[0:i] + temp_arr
    array = temp_arr
    return array

array = [1,3,2]
print(permu(array))
