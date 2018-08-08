__author__ = "Narwhale"

def binary_search(serach_list,serach_item):
    low = 0
    high = len(serach_list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = serach_list[mid]
        if guess == serach_item:
            return mid
        elif guess < serach_item:
            low = mid + 1
        elif guess > serach_item:
            high = mid - 1
    return None


my_list =[1,2,3,4,5,6,7,8,9,10]
print(binary_search(my_list,8))