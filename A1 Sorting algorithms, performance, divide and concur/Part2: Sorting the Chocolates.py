#Part 2: Sorting the chocolates by weight or price using merge sort›4
def merge_sort(chocolates, key=lambda x: x): #define the merge function
    if len(chocolates) <= 1: #Base case: list is already sorted if it has 1 or fewer elements
        return chocolates

    mid = len(chocolates) // 2  # Split the list into two halves
    left = merge_sort(chocolates[:mid], key) #recursively sort the left half
    right = merge_sort(chocolates[mid:], key) #recursively sort the right half

    merged_list = [] #merge the sorted left and right halves
    i = 0 #left index
    j = 0 #right index

    while i < len(left) and j < len(right): #Iterate while there are still elements in both left and right halves to compare
        if key(left[i]) <= key(right[j]):
            merged_list.append(left[i])
            i += 1 #Move to the next element in the left half

        else:
            merged_list.append(right[j])
            j += 1 #Move to the next element in the right half

    merged_list.extend(left[i:])
    merged_list.extend(right[j:])

    return merged_list #return the merged and sorted list


# Test cases used in part 1
chocolates_1 = [("Galaxy", "50g", 5, "milk chocolate"), ("Flutes", "30g", 3, "milk chocolate"), ("Kinder", "40g", 6, "white chocolate")]
chocolates_2 = [("Mars", "55g", 6, "milk chocolate"), ("Godiva", "60g", 20, "dark chocolate"), ("Dairy Milk", "45g", 4, "milk chocolate"), ("KitKat", "35g", 3, "milk chocolate")]
chocolates_3 = [("Snickers", "30g", 5, "milk chocolate"), ("Hershey's", "40g", 4, "dark chocolate")]

# Sort by weight
print("Chocolates_1 sorted by weight:")
print(merge_sort(chocolates_1, key=lambda x: x[1]))  # Sort by weight (found at index 1)

print("Chocolates_2 sorted by weight:")
print(merge_sort(chocolates_2, key=lambda x: x[1]))  # Sort by weight (found at index 1)

print("Chocolates_3 sorted by weight:")
print(merge_sort(chocolates_3, key=lambda x: x[1]))  # Sort by weight (found at index 1)

# Sort by price
print("Chocolates_1 sorted by price:")
print(merge_sort(chocolates_1,key=lambda x: x[2]) ) # Sort by price (found at index 2)

print("Chocolates_2 sorted by price:")
print(merge_sort(chocolates_2, key=lambda x: x[2]))  # Sort by price (found at index 2)

print("Chocolates_3 sorted by price:")
print(merge_sort(chocolates_3, key=lambda x: x[2]))  # Sort by price (found at index 2)
