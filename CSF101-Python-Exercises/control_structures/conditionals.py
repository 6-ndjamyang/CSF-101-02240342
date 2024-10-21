number = 10
if number > 0:
    print("The number is positive.")
else:
    print("The number is non-positive.")


number = 0
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is non-positive")
else:
    print("The number is Zero")

score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
    print(f"Your grade is : {grade}")
