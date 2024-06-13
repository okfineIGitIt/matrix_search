# Objective: Develop an algorithm, accompanied by unit tests, that fulfills the following
# requirements:
# 1. The algorithm should be capable of searching a matrix (of dimensions m x n) for a
# specified number. If the target number is found within the matrix, the algorithm should
# return true; otherwise, it should return false.
# 2. The time complexity of the algorithm should be logarithmic, i.e., O(log(N)), or better.
# 3. The algorithm should accurately log its execution time in microseconds.
# 4. The matrix for this task has the following characteristics:
# • Each row within the matrix is sorted in ascending order.
# • The first number of each row is larger than the last number of the preceding row.
# 5. You may use any programming language and unit testing framework of your choice.

def search_row(row, val):
  startIdx = 0
  endIdx = len(row) - 1

  # Since it's ascending order we can do a bisecting sort of search, should be reduce search time to n/2
  while (startIdx != endIdx):
    if row[startIdx] >= val:
      endIdx = startIdx + int((endIdx - startIdx) / 2)
    else:
      startIdx = endIdx - int((endIdx - startIdx) / 2)

  if row[startIdx] == val:
    return True
  
  return False
  

def search_matrix(mat, searchVal):
  """

  list mat: 2D matrix
  int searchVal: value to search for in list
  """
  # check matrix
  # if (not isinstance(mat, list)) or (len(mat) <= 0) or (not isinstance(mat[0], list)) or (len(mat[0]) <= 0):
  #   return False

  # we know
  # 1) each row is sorted in ascending order
  # 2) first number in each row is larger than the last number of the preceding row

  # meaning, if the last number in the row is larger (or equal to) the target value, the target must be in that row.
  for row in mat:
    if row[-1] >= searchVal: # value has to be in that row
      return search_row(row, searchVal)
  
  return False
