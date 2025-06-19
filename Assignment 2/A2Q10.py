def contact_list():
    contacts = (("Anil", "9876543210"), ("Priya", "9123456780"))
    for contact in contacts:
        print(f"Name: {contact[0]}, Phone: {contact[1]}")

contact_list()
