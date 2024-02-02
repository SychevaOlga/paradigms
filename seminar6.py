def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Пример использования
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7

index = binary_search(arr, target)
if index != -1:
    print("Искомый элемент найден по индексу", index)
else:
    print("Искомый элемент не найден")
