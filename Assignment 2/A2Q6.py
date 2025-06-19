def count_high_scores():
    marks = (67, 88, 92, 74, 76, 55)
    count = sum(1 for m in marks if m > 75)
    print(f"Students scoring above 75: {count}")

count_high_scores()
