"""Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers. """

def miniMaxSum(arr):
    for i in range(0, len(arr)):
        arr[i] = int(arr[i])
    s = sum(arr)
    print(str(s - max(arr)) + " " + str(s - min(arr)))
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
