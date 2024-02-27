#Part 1: Chocolate distribution algorithm: iterative and recursive functions
def distribute_iterative(chocolates, students):  # defines the iterative function
    if len(chocolates) < len(students):  # checks if there are enough chocolates for each student.
        return "Not enough chocolates for each student"  # return a message if there are not enough chocolates.

    distribution = []  # initialize an empty list to store the distribution of chocolates to students.
    for i in range(len(students)):  # iterate over the indices of the students list.
        distribution.append((students[i], chocolates[i]))  # pair each student with a chocolate and append to distribution list.

    return distribution  # return the distribution of chocolates to students.


def distribute_recursive(chocolates, students, result=[]): #defines the recursive function
    if len(students) == 0: # base case: no students left
        return result

    if len(students) <= len(chocolates):  # checks if there are enough chocolates for each student.
        return [(students[0], chocolates[0])] + distribute_recursive(chocolates[1:], students[1:])  # pairs the first student with the first chocolate and recursively distribute the remaining chocolates and students.
    else:
        return "Not enough chocolates for each student"  # return a message if there are not enough chocolates.

#Test case 1
chocolates_1 = [("Galaxy", "50g", 5, "milk chocolate"), ("Flutes", "30g", 3, "milk chocolate"), ("Kinder", "40g", 6, "white chocolate")]
students = ["Hamdan", "Khaled", "Abdulla"]  # list of students

print("Iterative distribution: ", distribute_iterative(chocolates_1, students))  # returns the list of chocolate with students through the iterative function
print("Recursive distribution: ", distribute_recursive(chocolates_1, students))  # returns the list of chocolate with students through the recursive function

#Test case 2
chocolates_2 = [("Mars", "55g", 6, "milk chocolate"), ("Godiva", "60g", 20, "dark chocolate"), ("Dairy Milk", "45g", 4, "milk chocolate"), ("KitKat", "35g", 3, "milk chocolate")]
students = ["Wafa", "Shamma", "Shahad", "Shouq"] #list of students

print("\nIterative distribution: ", distribute_iterative(chocolates_2, students)) #returns the list of chocolate with students through the iterative function
print("Recursive distribution: ", distribute_recursive(chocolates_2, students)) #returns the list of chocolate with students through the recursive function

#Test case 3
chocolates_3 = [("Snickers", "30g", 5, "milk chocolate"), ("Hershey's", "40g", 4, "dark chocolate")]
students = ["Mohammed", "Zayed"] #list of students

print("\nIterative distribution: ", distribute_iterative(chocolates_3, students)) #returns the list of chocolate with students through the iterative function
print("Recursive distribution: ", distribute_recursive(chocolates_3, students)) #returns the list of chocolate with students through the recursive function