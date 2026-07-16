emp = []

while True:
    print("\n1. Create")
    print("2. Update")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    b = int(input("Enter the option: "))

    match b:
        case 1:
            employee = {}
            employee["id"] = int(input("Enter employee id: "))
            employee["name"] = input("Enter employee name:")
            employee["department"] = input("Enter department:")
            employee["salary"] = float(input("Enter salary:"))

            emp.append(employee)


        case 2:
            print("Employees:", emp)
            old = input("Enter the employee name to update: ")
            if old in emp:
                new = input("Enter the new employee name: ")
                index = emp.index(old)
                emp[index] = new
                print("Employee updated successfully.")
            else:
                print("Employee not found.")

        case 3:
            print("Employees:", emp)
            name = input("Enter the employee to delete: ")
            if name in emp:
                emp.remove(name)
                print("Employee deleted successfully.")
            else:
                print("Employee not found.")

        case 4:
            print("Employee List:", emp)

        case 5:
            print("Exiting...")
            break

        case _:
            print("Invalid option.")