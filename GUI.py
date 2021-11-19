# Authors: Oscar Cabrera & Mikhail Tinio
# Filename: GUI.py
# Created: Oct 19, 2021
# Notes: This is for the designer


from easygui import *
import sys


class GUI():
        
    def drinkType(self):
        msg = "Choose a drink type"
        title = "QRbucks Designer"
        choices = ["Hot Coffee", "Hot Drink", "Cold Coffee", "Cold Drink", \
                   "Hot Tea", "Frappuccino", "Iced Tea"]
        choice = choicebox(msg, title, choices)
        
        # if the choice exists, return choice
        if choice:
            return choice
        # if the choice does not exist, stop the program
        else:
            sys.exit(0)
    
    
    def drinkCoffeeTypes(self):
        msg = "choose a drink a type"
        title = "QRbucks designer"
        choices = ["Americanos", "Brewed Coffes", "Cappuccinos",
                   "Espreso Shots", "Flat Whites", "Lattes", "Macchiatos", \
                   "Mochas"]
        choice = choicebox(msg, title, choices)
        
        if choice:
            return choice
        else:
            sys.exit(0)
    
    
    def drinkSize(self):
        msg = "Choose a drink size"
        title = "QRbucks Designer"
        choices = ["Short", "Tall", "Grande", "Venti"]
        choice = choicebox(msg, title, choices)
        
        if choice:
            return choice
        else:
            sys.exit(0)
    
    
    def drinkCream(self):
        msg = "choose a Cream"
        title = "QRbucks designer"
        choices = ["Default", "Oatmilk", "Nonfat Milk",
                   "Whole Milk", "Heavy Cream", "Coconut", "Sweet Cream", \
                   "2% Milk", "Half Cream", "Almond Milk", "Soymilk"]
        choice = choicebox(msg, title, choices)
        
        if choice:
            return choice
        else:
            sys.exit(0)
    
    
    def drinkFlavors(self):
        msg = "choose a Flavor"
        title = "QRbucks designer"
        choices = ["Default", "Syrup", "Apple Brown Sugar",
                   "Brown Sugar", "Caramel", "Cinnamon", "Cinnamon Dolce", \
                   "Funnel Cake" , "Hazelnut", "Peppermint", "Raspeberry", \
               "Toffee Nut", "Vanilla", "Sugar Free Vanilla", "Sauces", \
               "Dark Caramel", "Pumpkin", "White Chocolate Mocha"]
        choice = choicebox(msg, title, choices)
        
        if choice:
            return choice
        else:
            sys.exit(0)
    
    def drinkFrappuccino():
        msg = "choose a Frappuccino"
        title = "QRbucks designer"
        choices = ["Sugar Cookie Almondmilk Frappuccino Blended Beverage", "Toasted White Chocolate Mocha Frappuccino Blended Beverage",
                   "Peppermint White Chocolate Mocha Frappuccino Blended Beverage", "Caramel Brulee Frappucino Blended Beverage",
                   "Peppermint Mocha Frappuccino Blended Beverage", "Apple Crisp Frappuccino Blended Beverage",
                   "Mocha Cookie Crumble Frappuccino Blended Beverage", "Chestnut Praline Frappuccino Blended Beverage",
                   "Caramel Ribbon Crunch Frappuccino Blended Beverage", "Espresso Frappuccino Blended Beverage",
                   "Caffe Vanilla Frappuccino Blended Beverage", "Caramel Frappuccino Blended Beverage", "Coffe Frappuccino Blended Beverage",
                   "Mocha Frappuccino Blended Beverage", "Java Chip Frappuccino Blended Beverage",
                   "White Chocolate Mocha Frappuccino Blended Beverage"]
        choice = choicebox(msg, title, choices)
        
        if choice:
            return choice
        else:
            sys.exit(0)
    
    def drinkHotChocolate():
        msg = "choose a Hot Chocolate"
        title = "QRbucks designer"
        choices = ["Toasted White Hot Chocolate", "Peppermint White Hot Chocolate", "Peppermint Hot Chocolate",
                   "Hot Chocolate", "White Hot Chocolate"]
        choice = choicebox(msg, title, choices)
        
        if choice:
            return choice
        else:
            sys.exit(0)
    
    def drinkJuice():
        msg = "choose a Juice"
        title = "QRbucks designer"
        choices = ["Caramel Apple Spice", "Steamed Apple Juice"]
        choice = choicebox(msg, title, choices)
        
        if choice:
            return choice
        else:
            sys.exit(0)
    
    def drinkSteamers():
        msg = "choose a Steamers"
        title = "QRbucks designer"
        choices = ["Chestnut Preline Creme", "Caramel Brulee", "Pumpkin Spice Creme",
                   "Cinnamon Dolce Creme", "Steamed Milk", "Vanilla Creme"]
        choice = choicebox(msg, title, choices)
        
        if choice:
            return choice
        else:
            sys.exit(0)
    
    def drinkIcedTeas():
        msg = "choose an Iced Tea"
        title = "QRbucks designer"
        choices = ["Teavana Sparkling Unsweetened Peach Nectarine Green Tea", "Teavana Mango Balck Tea", "Iced Black Tea",
                   "Iced Black Tea", "Iced Royal English Breakfast Tea Latte", "Iced London Fog Tea Latte",
                   "Iced Chai Tea Latte", "Iced Peach Green Tea", "Iced Peach Green Tea Lemonade",
                   "Iced Matcha Tea Latte", "Iced Green Tea", "Iced Green Tea Lemonade", "Iced Matcha Lemonade",
                   "Iced Passion Tango Tea", "Iced Passion Tango Tea Lemonade"]
        choice = choicebox(msg, title, choices)
        
        if choice:
            return choice
        else:
            sys.exit(0)
    
    def toppings(self):
         msg = "Choose toppings"
         title = "QRbucks Designer"
         choices = ["None", "Cinnamon Delce Sprinkles", \
                   "Powdered Sugar Funnel Cake", "Pumpkin Spice", \
                   "Caramel Drizzle", "Mocha Drizzle", \
                   "Spiced Apple Drizzle", "Stawberry Drizzle" \
                   "Cinnamon Powder", "Whipped Cream", "Cold Foam", \
                   "Pumpkin Cream Cold Foam", "Salted Caramel Cream COld Foam", \
                   "Vanilla Sweet Cream Cold Foam"]
         choice = choicebox(msg, title, choices)
        
         if choice:
            return choice
        else:
            sys.exit(0)
    
    
    def sweetener(self):
        msg = "Choose a sweetener"
        title = "QRbucks Designer"
        choices = ["None", "Sugar", "Honey", "Stevia in the Raw", "Cane Sugar", \
                   "Sugar in the Raw", "Splenda", "Classic Syrup", "Honey Blend"]
        choice = choicebox(msg, title, choices)
        
        if choice:
            return choice
        else:
            sys.exit(0)


    def espressoShots(self):
        msg = "How many espresso shots"
        title = "QRbucks Designer"
        choices = ["None", "One", "Two", "Three", "Four"]
        choice = choicebox(msg, title, choices)
        
        if choice:
            return choice
        else:
            sys.exit(0)
    
    
    def confirmChoices(self):
        msg = "Do you want to proceed with your order?"
        title = "QRbucks Designer"
    
        if ccbox(msg, title):
            pass
        else:
            self.drinkCoffeeTypes()
