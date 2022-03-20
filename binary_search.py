from sys import argv, exit

def binary_search(sorted_list, search_number): # binary search algoritm
    
    high = len(sorted_list) - 1 # max lenght
    low = 0 # min lenght

    while low <= high:

        mid = (high + low) // 2 # search middle 
        if sorted_list[mid] == search_number:
            return mid
        elif sorted_list[mid] < search_number:
            low = mid + 1
        elif sorted_list[mid] > search_number:
            high = mid - 1

    return None



# input data
search_number = int(argv[1])

# set interval [ x to y ]
interval = [
    int(argv[2]), 
    int(argv[3])
]

# create sort list with interval
sorted_list = []
for i in range(interval[0], interval[1] + 1):
    sorted_list.append(i)

# check result
result = binary_search(sorted_list, search_number)
if result is not None:
    result_id_number = result
else:
    print(None)
    exit(0)

result_number = sorted_list[result_id_number]

print("[{};{}] array: {}".format(interval[0], interval[1], sorted_list))

if search_number == result_number:
    print("Success: search_number = {}, result_number = {}, id = {}".format(
        str(search_number),
        str(result_number),
        str(result_id_number)
        )
    )

else:
    print("Error: Values do not coincide\nsearch_number = {}, result_number = {}, id = {}".format(
        str(search_number),
        str(result_number),
        str(result_id_number)
        )
    )
