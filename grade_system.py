try:
    gradenumber = int(input("Enter your mark (0-100): "))

    if gradenumber >= 90 and gradenumber <= 100:
        print(f"Mark: {gradenumber} -> Grade: A")
    elif gradenumber >= 80 and gradenumber < 90:
        print(f"Mark: {gradenumber} -> Grade: B")
    elif gradenumber >= 70 and gradenumber < 80:
        print(f"Mark: {gradenumber} -> Grade: C")
    elif gradenumber >= 60 and gradenumber < 70:
        print(f"Mark: {gradenumber} -> Grade: D")
    elif gradenumber < 60:
        print(f"Mark: {gradenumber} -> Grade: E")
    else:
        print("invalid mark")
except:
    print("Something went wrong")
