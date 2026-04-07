

# 3rd task 

# english = int(input("Enter your English score: "))
# math  = int(input("enter the math marks"))
# physics = int(input("enter the physisc marks"))
# chemistry = int(input("enter the chemistry marks"))
# islamiat = int(input("enter the islamiat marks"))
# totalMarks = int(500);
# obtainMarks = int(english+math+physics+chemistry+islamiat);
# percentage = (obtainMarks/totalMarks)*100

# print("percentage",int(percentage),"%")


# number = 30.56
# number = int(number)
# print(type(number))





# first example of if and elif
# a = 10
# b = 10

# if a > b:
#  print("a is greated than b ")
# elif b > a:
#  print("b is greater than a")

# elif a == b:
#  print("a is equal to b")


# second example of if and elif

# a = 10
# b = 20

# if(a>=b):
#     print("a is greater than or equal to b")
# elif a<b:
#     print("a is less than b")


# third example of if and elif

# age = int(input("enter your age "))
# if age>18:
#     print("you are eligible for id card")
# elif age<18:
#     print("you are not eligible for id card")
# else:
#     print("the age is equalt to 18!")



# fourth 

computer_science = int(input("enter your computer_science marks "))
programming = int(input("enter your programming marks"));
Ai = int(input("enter your ai marks"))
social_science = int(input("enter your social_science marks"))

total = int(400)
obtain = int(computer_science+programming+Ai+social_science)
percentage = ((obtain/total)*100)

if(percentage==50 ):
    print("percentage is ",percentage,"%")
    print("you are pass",)
elif(percentage<=60):
    print("percentage is ",percentage,"%")
    print("your grad is B")
elif(percentage<=70):
    
    print("percentage is ",percentage,"%")
    print("your grade is A")
elif(percentage<=80):
    
    print("percentage is ",percentage,"%")
    print("your grade is A+")
else:
    print("you are fail")