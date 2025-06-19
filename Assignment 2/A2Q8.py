def average_temperature():
    temperatures = (29.5, 30.0, 32.2, 31.5, 28.9)
    avg = sum(temperatures) / len(temperatures)
    print("Temperature Readings:", temperatures)
    print("Average Temperature:", round(avg, 2))

average_temperature()
