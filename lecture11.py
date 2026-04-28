
# functions 
# function is a block of code that is used for writing once and use it everywhere 


# def 
# name of the function
# (): 
# block

# define the function , function declaration
# def printName()
#     print("hello python")
# }    
# # call the function , executing the function 
# printName()
# printName()
# printName()


# sum the variables in function 

# def sum():
#     x = int(input("enter value of x"));
#     y = int(input("enter the value of y"))
#     print("the sum of two variables is ",(x+y))
    
# sum() 




# passing function paramaters 

# def sum(x=4,y=9):
#     print("the sum of x and y is ",x+y)
# sum()


# passing arguments to the function 
# def sum(x,y,z):  # parameters 
#     print(x+y+z)


# Symb="Y"
# while Symb == "Y":
#     x = int(input("enter first value"))
#     y = int(input("enter the second value"))
#     z = int(input("enter the third value"))
#     sum(x,y,z)
#     Symb = input("do you want to continue! if yes then enter Y if not then enter N")



# return in function 


# def sum():
#     x=4
#     y=6
#     print(x+y)   #10
    
# sum()





# def sum():
#     y = 4
#     x = 5
#     return x+y

# store = sum()+4
# print(store)    


students_data = {
    "student1":{
        "role_no":"2012118",
        "name":"Ameen",
        "age":25,
        "Address":"TandoAllhyar"
    },
    "student2":{
        "role_no":"2012119",
        "name":"Tanzeel",
        "age":43,
        "Address":"Karachi"
    },
    "student3":{
        "role_no":"2012120",
        "name":"faizan",
        "age":35,
        "Address":"Hyderabad"
    }
    
}
 
def showStudentsData(data,roleNo):
             flag="F";
             for key,value in data.items():
                 
                 if(value["role_no"] == roleNo):
                      flag="T"
                      print("student found",value)
                      
             if(flag=="F"):
                print("student not found")
 
 
role_no = input("enter studnet role number please ")           
showStudentsData(students_data,role_no)        