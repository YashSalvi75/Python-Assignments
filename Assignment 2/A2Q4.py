def train_schedule():
    schedule = (("Rajdhani", "10:00"), ("Shatabdi", "12:30"), ("Duronto", "17:00"))
    for train in schedule:
        print(f"Train: {train[0]}, Time: {train[1]}")

train_schedule()
