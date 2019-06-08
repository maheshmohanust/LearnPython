def print2largest(arr, arr_size):
    if arr_size < 2:
        print(" Invalid Input ")
        return
    temp = -2147483648
    first = second = temp
    for i in range(arr_size):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] != first:
            second = arr[i]
    if second == temp:
        print("There is no second largest element")
    else:
        print("The second largest element is:", second)


array = [12, 35, 1, 10, 34, 1]
n = len(array)
print2largest(array, n)
