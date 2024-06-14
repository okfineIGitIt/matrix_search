import time

import matrix_search

test_mat_notmat = "asldjasd"
test_mat_2_mat1D = [1, 2, 3]
test_mat_3_mat2D_no_elements = [[]]
test_mat_4_norm = [
  [1, 2, 3]
]
test_mat_5_norm = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

test_mat_6_norm = [
  [1, 1, 1],
  [2, 2, 2]
]

test_mat_6_norm = [
  [1, 1, 1],
  [2, 2, 2],
  [3, 3, 3]
]

test_mat_7_one_element = [
  [1]
]

rows = 10000
cols = 10000
start = 0
end = cols
test_mat_8_big1 = []
for row_idx in range(0, rows):
  test_mat_8_big1.append(list(range(start, end)))
  start = start + cols
  end = end + cols

if __name__ == "__main__":
  # [test name, matrix to test, searchValue, expected result]
  test_list = [
    ["Not a matrix", test_mat_notmat, 2, False],
    ["1D", test_mat_2_mat1D, 2, False],
    ["2D no elements", test_mat_3_mat2D_no_elements, 7, False],
    ["Normal matrix search val absent", test_mat_4_norm, 0, False],
    ["Normal matrix search val present", test_mat_4_norm, 1, True],
    ["Normal matrix search val present", test_mat_5_norm, 5, True],
    ["Normal matrix row is one element", test_mat_6_norm, 2, True],
    ["2D one element (exists)", test_mat_7_one_element, 1, True],
    ["test_mat_7_one_element (absent)", test_mat_7_one_element, 2, False],
    ["test_mat_8_big1", test_mat_8_big1, 50000, True]
  ]

  for name, test_mat, test_val, expectedResult in test_list:
    start_time = time.perf_counter_ns()
    result = matrix_search.search_matrix(test_mat, test_val)
    end_time = time.perf_counter_ns()

    print(f"{name}: {(end_time - start_time) / 1000} us")
    assert(result == expectedResult)

  print("All tests passed!")
