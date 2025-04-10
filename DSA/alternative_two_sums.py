def twosums():
  for i in range(len(array)):
    j= i+1
    for j in range(len(array)-1):
        if array[i] + array[j] == targetSum:
            output = array[i], array[j]
    return output
