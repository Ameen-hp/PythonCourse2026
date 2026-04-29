# Default parameters 

# def display(arg="hellow"):
#     print(arg)
# display()    



# arguments length




# def printNumbers(num1,num2,num3):
#     store = num1+num2+num3
#     print(store)
    
# printNumbers(3,4,6,5)    

product1 = [
    {
        "product_id": "PRD-001",
        "name": "Ultra-Lite Running Shoes",
        "category": "Footwear",
        "price": 89.99,
        "stock_quantity": 120,
        "rating": 4.7,
        "is_active": True,
        "tags": ["fitness", "sports", "apparel"]
    },
    {
        "product_id": "PRD-002",
        "name": "Smart-Watch Pro X",
        "category": "Electronics",
        "price": 249.50,
        "stock_quantity": 45,
        "rating": 4.2,
        "is_active": True,
        "tags": ["tech", "wearable", "gadget"]
    },
    {
        "product_id": "PRD-003",
        "name": "Organic Roasted Coffee (500g)",
        "category": "Groceries",
        "price": 18.00,
        "stock_quantity": 300,
        "rating": 4.9,
        "is_active": True,
        "tags": ["organic", "beverage", "fair-trade"]
    },
    {
        "product_id": "PRD-004",
        "name": "Noise Cancelling Headphones",
        "category": "Electronics",
        "price": 129.99,
        "stock_quantity": 15,
        "rating": 4.5,
        "is_active": False,
        "tags": ["audio", "office", "travel"]
    },
    {
        "product_id": "PRD-005",
        "name": "Ergonomic Office Chair",
        "category": "Furniture",
        "price": 310.00,
        "stock_quantity": 8,
        "rating": 4.8,
        "is_active": True,
        "tags": ["home-office", "furniture", "comfort"]
    }
]

storeCustomCategoriesProducts = []

def findTheMaximumPriceOfProduct(category):
        for subProduct in product1:
              if(subProduct["category"] == category):
                  storeCustomCategoriesProducts.append(subProduct)
 
findTheMaximumPriceOfProduct("Electronics")
# findTheMaximumPriceOfProduct("Furniture")
print(storeCustomCategoriesProducts)





# books = {
#      "book1": {
#       "name":"phsyics",
#       "price":200
#      },
#      "book2": {
#       "name":"mathematics",
#       "price":300
#      }
# }

# books.update({"book3": {
#       "name":"python",
#       "price":400
#      }})
     
     
# print(books)