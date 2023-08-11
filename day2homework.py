# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a, b, c):
    return max(a, b, c)


print(max_num(4, 56, 35))
print(max_num(4, 25, 13))

# Write a Python function called mult_list() to multiply all the numbers in a list.


def mult_list(list):
    result = 1
    for x in list:
        result = result * x
    return result


list1 = [1, 3, 5, 2]

print(mult_list(list1))
# Write a Python function called rev_string() to reverse a string.


def rev_string(txt):
    return txt[::-1]


print(rev_string("hello world"))

# Write a Python function called num_within() to check whether a number falls in a given range.

# Does not return 15 as 'in range'
# def num_within(num):
#     if num in range(4, 15, 2):
#         print("number is in range")
#     else:
#         print("number is out of range")


def num_within(x, a, b):
    return x in range(a, b+1)


# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
print(num_within(3, 2, 4))
print(num_within(3, 1, 3))
print(num_within(10, 2, 5))


# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
triangle = [[1], [1, 1]]


def pascal(n):
    # base case
    if n < 1:
        print("invalid number of rows")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        # fill up correct number of rows in triangle
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]
            # create correct row, then add to triangle (this row will be 1 longer than row before it)
            length = len(row_prev)+1
            for i in range(length):
                # first number is 1
                if i == 0:
                    row.append(1)
                # intermediate nunmbers get added from previous rows
                elif i > 0 and i < length-1:
                    row.append(triangle[row_number-1]
                               [i-1]+triangle[row_number-1][i])
                # last number is 1
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1

        # print triangle
        for row in triangle:
            print(row)


pascal(2)
pascal(5)
