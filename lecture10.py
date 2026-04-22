# dictionaries 
# object => attributes 
# changeble,ordered,dont allows dupplicates
# car = {
#   "color":"red",
#   "model":2020,
#   "registration_number":"45BKL",
#   "makker":"honda",
# }

# print(car)

# # print any key from the dictionary
# print(car["model"])
# # print all the keys of dictioanry
# print(car.keys())
# # print all values in the dictionary
# print(car.values())
# # print both keys and values 
# print(car.items())



# how to print using loop

# for x in car.values():
#     print(x);


# for x in car.keys():
#     print(x);


# print keys and values both from the car

# for x,y in car.items():
#     print(x,y)


# how to change an element in the dictionary

# car["model"] = 2021
# print(car)


# change by update method 

# car.update({"color":"white"})
# print(car)


# how to remove 

# car.pop("color")
# print(car)

# clear all the dictionary
# car = car.clear()
# print(car)


# how to copy an dictianary

# car2 = car.copy()
# print(car2)



# nested dictianry
car = {
  "color":"red",
  "model":2020,
  "registration_number":"45BKL",
  "makker":"honda",
  "engine":{
      "color":"red",
      "engine_number":"12321BK",
      "weight":"90kg"
  }
}

print(car["engine"]["engine_number"])