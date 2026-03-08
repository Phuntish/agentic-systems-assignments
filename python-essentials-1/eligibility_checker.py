try:
    print("please enter your name")
    name = input()

    print("please enter your age")
    age = int(input())

    if age < 0:
        print("Age cannot be negative")
    else:
        if(age<13):
            print("You are a Child ")
        elif(age>=13 and age <=17):
            print("You are a Teenager ")
        elif(age>=18 and age <=59):
            print("You are an Adult ")
        else:
            print("You are Senior Citizen ")
    

    if age >= 18:
        print("and you are eligible to vote")
    else:
        print("and you are not eligible to vote")
    

except ValueError:
    print("Invalid age input")