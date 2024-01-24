class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id}\t{self.name}\t{self.age}\t{self.salary}"

def sort_employees(employees, key):
    return sorted(employees, key=lambda emp: getattr(emp, key))

if __name__ == "__main__":
    employee_data = [
        Employee("161E90", "Ramu", 35, 59000),
        Employee("171E22", "Tejas", 30, 82100),
        Employee("171G55", "Abhi", 25, 100000),
        Employee("152K46", "Jaya", 32, 85000),
    ]

    print("Choose sorting parameter:")
    print("1. Age\n2. Name\n3. Salary")

    choice = int(input())

    if choice == 1:
        sorted_employees = sort_employees(employee_data, "age")
    elif choice == 2:
        sorted_employees = sort_employees(employee_data, "name")
    elif choice == 3:
        sorted_employees = sort_employees(employee_data, "salary")
    else:
        print("Invalid choice. Please choose a valid option.")
        exit()

    print("\nSorted Employee Data:")
    print("Employee ID\tName\tAge\tSalary")
    for employee in sorted_employees:
        print(employee)
