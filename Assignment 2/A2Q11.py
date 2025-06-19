def exam_schedule():
    exams = (("Math", "9:00 AM"), ("Science", "11:30 AM"), ("English", "2:00 PM"))
    for exam in exams:
        print(f"Subject: {exam[0]}, Time: {exam[1]}")

exam_schedule()
