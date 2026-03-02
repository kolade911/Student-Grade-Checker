name = input("Enter your name: ")

math = int(input("Enter your maths score: "))
english = int(input("Enter your english score: "))
science = int(input("Enter your science score: "))


average = (math + english + science) / 3

#Grade System

if average >= 70:
    print("Grade : A")

elif average >= 50:
    print("Grade : B")

elif average >= 49:
    print("Grade : C")

elif average >= 40:
    print("Grade : D")
elif average >= 30:
    print("Grade : E")
else:
    print("Grade : F")


#Status

if average >= 50:
    print("Status: Pass!")
else:
    print("Status : Fail!")


#Remarks

if average >= 80:
    print("Remark: Excellent! Keep it up.")
elif average >= 70:
    print("Remark: Very Good! Keep it up.")
elif average >= 50:
    print("Remark: Good effort! Keep it up.")
else:
    print("Remark: Needs Improvement! Don't give up.")


