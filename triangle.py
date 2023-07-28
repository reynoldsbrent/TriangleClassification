valid = False
while valid == False:
    angle_one = int(input("Please enter the first angle: "))
    angle_two = int(input("Please enter the second angle: "))
    angle_three = int(input("Please enter the third angle: "))
    sum = angle_one + angle_two + angle_three
    if sum == 180 and angle_one > 0 and angle_two > 0 and angle_three > 0:
        valid = True
    elif sum == 180 and (angle_one <= 0 or angle_two <= 0 or angle_three <= 0):
        print("Angles smaller than 0 are not valid.")
    else:
        print("The entered values are not valid.")

if angle_one == 90 or angle_two == 90 or angle_three == 90:
    print("The triangle is a right triangle.")
elif angle_one > 90 or angle_two > 90 or angle_three > 90:
    print("The triangle is an obtuse triangle.")
else:
    print("The triangle is an acute triangle.")