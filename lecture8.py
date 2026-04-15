

# Sequence => list,sets,tuples,
# # map => dictionaries

# collection of data types

# list 
# store the collection of data/values 
# ordered , changable,allows dupplicates 

# bookList=["programming book","introduction to computer","mathematics","english",12,3.5,True]
# print(bookList)
# how to access the list 
# index => position of an item
# print(bookList[4])

# knowing the length of list items

# print(len(bookList))
# print(type(bookList))


# accessig the piece of data by range 
# bookList=["programming book","introduction to computer","mathematics","english",12,3.5,True]
# print(bookList[1:5])  

# how  to change the list items 
# bookList=["programming book","introduction to computer","mathematics","english",12,3.5,True]
# bookList[0] = "phsyics book"
# bookList[3] = "pshycology"
# bookList[5] = 45

# to change the list items using range 
# bookList[2:5] = ["science","urdu",50]
# print(bookList)


# add,remove,insert 

# bookList=["programming book","introduction to computer","mathematics","english",12,3.5,True]
# append() => used to add an item in the list
# bookList.append("python book")
# print(bookList)

# insert() => insert items based on the index
# bookList.insert(2,"sindhi book")
# print(bookList)


# extend() => extend an list inside another list 
# bookList=["programming book","introduction to computer","mathematics","english",12,3.5,True]
# teachers = ["x","y","z","zx","zy"]

# bookList.extend(teachers)

# print(bookList)



# how to delete the items of an list 

# bookList=["programming book","introduction to computer","mathematics","english",12,3.5,True]
# # bookList.remove("programming book")
# # bookList.pop(4)
# del bookList[3]
# print(bookList)



#  how to print the list using for loop 
# bookList=["programming book","introduction to computer","mathematics","english",12,3.5,True]

# for x in bookList:
#     print(x);



bookList=["programming book","introduction to computer","mathematics","english",12,3.5,True]
for  items in bookList:
    
    if(items == "mathematics"):
        bookList.append("urdu")
    print(items)
print("i am out of the block")