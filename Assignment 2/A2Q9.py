def show_appointments():
    appointments = (("Doctor", "10:00 AM"), ("Meeting", "2:00 PM"))
    for appt in appointments:
        print(f"Appointment: {appt[0]}, Time: {appt[1]}")

show_appointments()
