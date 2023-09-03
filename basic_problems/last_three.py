from last_three_method import *
assert (unique([1, 2, 2, 3, 4, 4, 5]) == ([1, 2, 3, 4, 5]))
assert (dups([1, 2, 2, 3, 4, 4, 5]) == ([2, 4]))
assert (group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
assert (group([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]])