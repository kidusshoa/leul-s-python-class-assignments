employees = {
    "seid": [10000, 0.05, 5000],
    "chala": [2000, 0.05, 5000],
    "abenezer": [4000, 0.05, 5000],
    "abel": [20000, 0.05, 5000],
    "kebede": [8000, 0.05, 5000],
    "mohammed": [5000, 0.05, 5000]
}

def calculate_salaries():
    for name, details in employees.items():
        sell, percent, fixed_salary = details
        total_salary = fixed_salary + (sell * percent)
        details.append(total_salary)

def display_salaries():
    print("\nName\tTotal Salary")
    for name, details in employees.items():
        print(f"{name.capitalize()}\t{details[3]}")

def top_3_employees():
    top_3 = sorted(employees.items(), key=lambda x: x[1][3], reverse=True)[:3]
    print("\nTop 3 Highly Paid Employees:")
    for name, details in top_3:
        print(f"{name.capitalize()}: {details[3]}")

def salaries_above_5500():
    print("\nEmployees with Salary > 5500:")
    for name, details in employees.items():
        if details[3] > 5500:
            print(f"{name.capitalize()}: {details[3]}")

def main():
    calculate_salaries()  

    while True:
        print("\n=== Employee Salary Management ===")
        print("1. Display Salaries")
        print("2. Show Top 3 Highly Paid Employees")
        print("3. Show Employees with Salary > 5500")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            display_salaries()
        elif choice == '2':
            top_3_employees()
        elif choice == '3':
            salaries_above_5500()
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
