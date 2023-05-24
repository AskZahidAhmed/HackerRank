"""Problem Statement
There is a horizontal row of n cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if cubei is on top of cubej then sideLengthj≥sideLengthi.
When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.
Input Format
The first line contains a single integer T, the number of test cases. 
For each test case, there are 2 lines. 
The first line of each test case contains n, the number of cubes. 
The second line contains n space separated integers, denoting the sideLengths of each cube in that order.
Constraints 
1≤T≤5 
1≤n≤105 
1≤sideLength<231
Output Format
For each test case, output a single line containing either "Yes" or "No" without the quotes.
Sample Input
2
6
4 3 2 1 3 4
3
1 3 2
Sample Output
Yes
No
Explanation
In the first test case, pick in this order: left - 4, right - 4, left - 3, right - 3, left - 2, right - 1. 
In the second test case, no order gives an appropriate arrangement of vertical cubes. 3 will always come after either 1 or 2."""

def can_pile_cubes(cube_lengths):
    cube_on_top = None
    left_index = 0
    right_index = len(cube_lengths) - 1

    while left_index < right_index:  # Avoid corner case of `cube_lengths` being an empty list
        left_cube = cube_lengths[left_index]
        right_cube = cube_lengths[right_index]

        if cube_on_top is None:
            if left_cube > right_cube:
                cube_on_top = left_cube
                left_index += 1
            else:
                cube_on_top = right_cube
                right_index -= 1
        else:
            if left_cube > right_cube:
                if left_cube > cube_on_top:
                    return False
                cube_on_top = left_cube
                left_index += 1
            else:
                if right_cube > cube_on_top:
                    return False
                cube_on_top = right_cube
                right_index -= 1

    return True


def parse_test_case():
    input()  # Throw away number of cubes
    return [int(x) for x in input().split()]


if __name__ == '__main__':
    num_tests = int(input())
    for _ in range(num_tests):
        can_pile = can_pile_cubes(parse_test_case())
        print('Yes' if can_pile else 'No')

