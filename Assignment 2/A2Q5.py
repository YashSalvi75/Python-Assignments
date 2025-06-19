def sort_employees():
    employees = (("John", 40000), ("Alice", 55000), ("Raj", 30000))
    sorted_employees = sorted(employees, key=lambda x: x[1])
    for emp in sorted_employees:
        print(f"{emp[0]}: ₹{emp[1]}")

sort_employees()
