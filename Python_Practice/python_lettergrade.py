#What is the score?
score = int(input("What is your test score?"))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is an B.')
elif score >=70:
    print('Your grade is an C.')
elif score >= 60:
     print('Your grade is an D.')
else:
    print('Your grade is an F.')