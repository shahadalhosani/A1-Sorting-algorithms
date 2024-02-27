#Code for Part2 is included here to ensure that merge_sort is defined.
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

#Part3: Searching for a specific chocolate using the binary search function
def binary_search(chocolates, value, key=lambda x: x): #define the binary search function, including three parameters
    low, high = 0, len(chocolates) - 1 #Initialize the low and high indices for the search interval

    while low <= high: #perform binary search while the search interval is valid
        mid = (low + high) // 2 # Calculate the midpoint index of the current search interval
        mid_value = key(chocolates[mid]) #Extract the weight or price of the chocolate at the midpoint using the key function

        if mid_value == value: # Check if the midpoint weight or price is equal to the target weight or price
            return mid  # Return index if chocolate is found
        elif mid_value < value:
            low = mid + 1 #If the midpoint weight or price is less than the target weight or price, update the low index
        else:
            high = mid - 1 #If the midpoint weight or price is greater than the target weight or price, update the high index

    return None #If the chocolate with the target weight or price is not found, return None


# Test Case 1
chocolates = [("Galaxy", "50g", 5, "milk chocolate"), ("Flutes", "30g", 3, "milk chocolate"), ("Kinder", "40g", 6, "white chocolate")] #list of chocolates
student_names = ["Hamdan", "Khaled", "Abdulla"] #list of students
sorted_chocolates_by_weight = merge_sort(chocolates, key=lambda x: x[1])  # Sort by weight (index 1)

# Search for chocolate with weight "30g"
result = binary_search(sorted_chocolates_by_weight, "30g", key=lambda x: x[1])
chocolate_name, student_name = sorted_chocolates_by_weight[result][0], student_names[result]  # gives the corresponding chocolate and student's name
print(f"The student holding the chocolate '{chocolate_name}' with the weight of 30g is '{student_name}'.") #Print the result if the chocolate is found.


# Test case 2
chocolates = [("Mars", "55g", 6, "milk chocolate"), ("Godiva", "60g", 20, "dark chocolate"), ("Dairy Milk", "45g", 4, "milk chocolate"), ("KitKat", "35g", 3, "milk chocolate")]
student_names = ["Wafa", "Shamma", "Shahad", "Shouq"] #list of students
sorted_chocolates_by_price = merge_sort(chocolates, key=lambda x: x[2])  # Sort by price (index 2)

# Search for chocolate with price "6dhs"
result = binary_search(sorted_chocolates_by_price, 6, key=lambda x: x[2])
chocolate_name, student_name = sorted_chocolates_by_price[result][0], student_names[result] # gives the corresponding chocolate and student's name
print(f"The student holding the chocolate '{chocolate_name}' with the price of 6 is '{student_name}'.")