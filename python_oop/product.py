# Assignment: Product
# Objectives:
# Practice creating a class and making instances from it
# Practice accessing the methods and attributes of different instances
# Practice altering an instance's attributes
# The owner of a store wants a program to track products. Create a product class to fill the following requirements.

# Product Class:
# Attributes:

# Price
# Item Name
# Weight
# Brand
# Status: default "for sale"
# Methods:

# Sell: changes status to "sold"
# Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
# Return Item: takes reason_for_return as a parameter and changes status accordingly. If the item is being returned because it is defective, change status to "defective" and change price to 0. If it is being returned in the box, like new, mark it "for sale". If the box has been opened, set the status to "used" and apply a 20% discount.  (use "defective", "like_new", or "opened" as three possible value for reason_for_return).
# Display Info: show all product details.
# Every method that doesn't have to return something should return self so methods can be chained.

class Product:
    def __init__(self,itemName,price,weight, brand):
        self.itemName=itemName
        self.price=price
        self.weight=weight
        self.brand=brand
        self.status="For Sale"

    def sell(self):
        self.status="sold"
        return self
    def addTax(self,tax):
        self.price=self.price+(self.price * tax)
        return self
    def returnItem(self,reason_for_return):
        if reason_for_return== "defective":
            self.status="defective"
            self.price=0
        if reason_for_return == "like new":
            self.status="for sale"
        if reason_for_return=="opened":
            self.status="used"
            self.price=self.price - (self.price * 0.20)
        return self
    def displayInfo(self):
        print("Price:",str(self.price))
        print("Item Name:",str(self.itemName))
        print("Weight:",str(self.weight))
        print("Brand:",str(self.brand))
        print("Status: " + str(self.status))
        return self

product_one = Product("Peas", 3.99, 0.16, "Green Giant")
product_one.displayInfo() .returnItem("opened") .displayInfo()

product_two = Product("Forks", 7.99, 0.75, "Select Kitchen")
product_two.displayInfo() .returnItem("like new") .displayInfo()

product_three = Product("Diapers", 33.99, 4.25, "Huggies")
product_three.displayInfo() .returnItem("defective") .displayInfo()

product_four = Product("Crayons", 4.99, 0.25, "Crayola")
product_four.displayInfo() .addTax(0.12) .displayInfo()

product_five = Product("Crayons", 4.99, 0.25, "Crayola")
product_five.displayInfo() .sell() .displayInfo()

