def binarySearch(array, key):
    comprimento = len(array)
    left = 0
    right = length - 1

    while (left <= right):
        middle = int((left + right)/2)
        if array[middle] == key:
            print(meio)
            break
        if key < array[middle]:
            right = middle - 1
        if key > array[middle]:
            left = middle + 1
        else:
            print("Value not found")

m=[1,3,5,7,9,11,13,15]
key=7
binarySearch(m, key)
