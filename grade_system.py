def grade_calculator():
    try:
        mark = int(input("Enter your mark (0-100): "))

        if mark >= 90 and mark <= 100:
            grade="A"
        elif mark >= 80 and mark < 90:
            grade="B"
        elif mark >= 70 and mark < 80:
            grade="C"
        elif mark >= 60 and mark < 70:
            grade="D"
        elif mark < 60 and mark >= 0:
            grade="E"
        else:
            raise ValueError("Please provide mark between 0 - 100.")
        
    except ValueError as e:
            print("Value Error", e)

    except Exception as e:
        print("Something went wrong", e)
        
    else:
        print(f"Mark: {mark} -> Grade: {grade}")

    


grade_calculator()