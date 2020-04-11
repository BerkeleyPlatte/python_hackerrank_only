# Given a 2D Array, arr:

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0

# We define an hourglass to be a subset of values with indices falling in this pattern
# in arr's graphical representation:

# a b c
#   d
# e f g

# There are 16 hourglasses in arr, and an hourglass sum is the sum of an hourglass'
# values.  Calculate the hourglass sum for every hourglass in arr, then print the
# maximum hourglass sum.


def two_d_array(arr):
    hourglass_list = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            try:
                hourglass = [
                    arr[i][j], arr[i][j+1], arr[i][j+2],
                    arr[i+1][j+1],
                    arr[i+2][j], arr[i+2][j+1], arr[i+2][j+2]
                ]
                hourglass_list.append(sum(hourglass))
            except IndexError:
                break
    return max(hourglass_list)


lst = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

lst2 = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]

print(two_d_array(lst2))
