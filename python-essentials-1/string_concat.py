
try:
    print("enter your fist name : ")
    first_name = input()
    print("enter your last name : ")
    second_name = input()
    print("enter your age : ")
    age = int(input())
    age += 1


    print("Full Name : " + first_name + second_name)
    print ("you will be " + str(age) + " next year")

except ValueError:
    print("Invaid age Input")



