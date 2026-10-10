
def generate_report(name, score):

    print("\n===== PERFORMANCE REPORT =====")
    print("Name:", name)
    print("Score:", score)

    if score >= 90:
        print("Grade: A")
    elif score >= 75:
        print("Grade: B")
    elif score >= 60:
        print("Grade: C")
    else:
        print("Grade: D")