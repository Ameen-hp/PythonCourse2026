# list introduction,how to print the list items,change,insert,update,remove,iterate loop



# sort() to sort the items 

# numbers = [100,200,50,20,1000,2000]
# # accending order 
# numbers.sort()
# # decending order 
# numbers.sort(reverse=True)
# print(numbers)




# books = ["physics","english","mathematics"]

# books.sort(reverse=False) # accending order 
# books.sort()  # accending order
# print(books)

# # how to copy a list 
# book2 = books.copy()
# print(book2) 

# # join lists

# book3 = books+book2
# print(book3)



# touple
# collection of data type 
# features: ordered,allows dupplication,unchangable

# colors = ("red","yellow","white","blue")

# print(colors)
# print(colors[2])
# print(colors[1:3])


# why unchangable 

# colors = ("red","yellow","white","blue")
# colors[2] = "black"
# print(colors)


# colors = ("red","yellow","white","blue")
# print(type(colors))
# colors2 = list(colors)
# print(type(colors2))


# how to append,remove 


# colors = ("red","yellow","white","blue","red")
# # count()
# # index()
# print(colors.count("red"))
# print(colors.index("blue"))


# loop on touple

# colors = ("red","yellow","white","blue","red")
# for x in range(len(colors)):
#     print(colors[x])




# while loop 
# initialization,condition,increament

# i=1
# while(i<5):
#     print("hello am using while loop")
#     i= i+1;
# else:
#     print("your loop has been completed")



# feedback = "good"
# while(feedback =="good"):
#     print("you are the best")
#     good = input("please enter the deedback")




for x in range(3):
    print("ameen")
else:
    print("tanzeel")