# Authors: Oscar Cabrera & Mikhail Tinio
# Edited by Dalton Walker
# Filename: GUI.py
# Created: Oct 19, 2021
# Notes: This is for the designer

# "Generate and Read QR Code with Python"
# by AllTech
# https://www.youtube.com/watch?v=2QK942FPCw0


from easygui import *
import qrcode
import sys


class GUI():

    def drinkType(self):
        msg = "Choose a drink type"
        title = "QRbucks Designer"
        choices = ["Coffee", "Hot Drink", "Cold Drink", \
                   "Hot Tea", "Frappuccino", "Iced Tea"]
        choice = choicebox(msg, title, choices)


        # if the choice exists, return choice
        if choice:
            return choice

        # if the choice does not exist, stop the program
        else:
            sys.exit(0)


    def drinkCoffeeTypes(self):
        msg = "Choose a drink type"
        title = "QRbucks designer"
        choices = ["Americano", "Brewed Coffees", "Espresso", "Iced Coffee"]
        choice = choicebox(msg, title, choices)

        if choice:
            return choice
        else:
            sys.exit(0)


    def hotDrinkTypes(self):
        msg = "Choose a hot drink type"
        title = "QRbucks designer"
        choices = ["Hot Chocolate", "Steamer", "Juice"]
        choice = choicebox(msg, title, choices)

        if choice:
            return choice
        else:
            sys.exit(0)


    def drinkBrewed(self):
         msg = "Choose a brewed coffee"
         title = "QRbucks designer"
         choices = ['blonde roast', 'pike place roast', 'dark roast', 'decaf pike place roast',]
         choice = choicebox(msg, title, choices)

         if choice:
             return choice
         else:
             sys.exit(0)


    def drinkEspresso(self):
          msg = "Choose a brewed coffee"
          title = "QRbucks designer"
          choices = ['cappuccino', 'espresso', 'espresso con panna', 'flat white', 'honey almondmilk flat white', \
                     'pumpkin spice latte', 'honey oatmilk latte','latte', 'cinnamon dolce latte', \
                         'blonde vanilla latte', 'apple crisp macchiato', \
                     'caramel macchiato', 'espresso macchiato', 'mocha', 'white chocolate mocha']
          choice = choicebox(msg, title, choices)

          if choice:
              return choice
          else:
              sys.exit(0)


    def drinkIcedCoffee(self):
            msg = "Choose a brewed coffee"
            title = "QRbucks designer"
            choices = ['pumpkin cream cold brew', 'salted caramel cream cold brew', 'honey almondmilk cold brew', \
                       'cold brew', 'vanilla sweet cream cold brew', 'cold brew with milk', \
                       'honey almondmilk nitro cold brew', 'nitro cold brew', 'vanilla sweet cream nitro cold brew', \
                           'iced coffee', 'iced coffee with milk', 'iced brown sugar oatmilk shaken espresso', \
                               'iced chocolate almondmilk shaken espresso', 'iced shaken espresso']

            choice = choicebox(msg, title, choices)

            if choice:
                return choice
            else:
                sys.exit(0)


    def drinkHotTea(self):
            msg = "Choose a hot tea"
            title = "QRbucks designer"
            choices = ['chai tea', 'chai tea latte', 'earl grey tea', 'london fog tea latte', \
                       'royal english breakfast tea', 'royal english breakfast tea latte', \
                           'emperors clouds & mist', 'matcha tea latte', 'honey citrus mint tea', \
                               'jade citrus mint tea', 'mint majesty', 'peach tranquility']

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
        msg = "Choose a Cream"
        title = "QRbucks designer"
        choices = ["Default", "2%", "Whole", "Skim", "Almond",
                    "Oat", "Coconut", "Soy"]
        choice = choicebox(msg, title, choices)

        if choice:
            return choice
        else:
            sys.exit(0)


    def drinkFrappuccino(self):
        msg = "Choose a Frappuccino"
        title = "QRbucks designer"
        choices = ['pumpkin spice frappuccino', 'apple crisp frappuccino', 'strawberry funnel cake frappuccino', \
                   'mocha cookie crumble frappuccino', 'caramel ribbon crunch frappuccino', 'espresso frappuccino', \
            'caffe vanilla frappuccino', 'caramel frappuccino', 'coffee frappuccino', 'mocha frappuccino', \
            'java chip frappuccino', 'white chocolate mocha frappuccino', 'pumpkin spice creme frappuccino',\
            'apple crisp creme frappuccino', 'strawberry funnel cake creme frappuccino', \
            'chocolate cookie crumble creme frappuccino', 'caramel ribbon crunch creme frappuccino', \
            'strawberry creme frappuccino', 'chai creme frappuccino', 'double chocolatey chip creme frappuccino', \
            'match creme frappuccino', 'vanilla bean creme frappuccino', 'white chocolate creme frappuccino']
        choice = choicebox(msg, title, choices)

        if choice:
            return choice
        else:
            sys.exit(0)


    def drinkCold(self):
        msg = "Choose a Refresher, Water, or Milk"
        title = "QRbucks designer"
        choices = ['star drink', 'kiwi starfruit refresher', 'kiwi starfruit refresher lemonade', 'dragon drink',\
                   'mango dragonfruit refresher', 'mango dragonfruit refresher lemonade', 'pink drink', \
                     'strawberry acai refresher', 'strawberry acai refresher lemonade', 'violet drink', \
                         'very berry refresher', 'very berry refresher lemonade', 'blended strawberry lemonade', \
                             'lemonade', 'water', 'milk' ]
        choice = choicebox(msg, title, choices)

        if choice:
            return choice
        else:
            sys.exit(0)


    def drinkHotChocolate(self):
        msg = "Choose a Hot Chocolate"
        title = "QRbucks designer"
        choices = ["Toasted White Hot Chocolate", "Peppermint White Hot Chocolate", "Peppermint Hot Chocolate",
                   "Hot Chocolate", "White Hot Chocolate"]
        choice = choicebox(msg, title, choices)

        if choice:
            return choice
        else:
            sys.exit(0)

    def drinkJuice(self):
        msg = "Choose a Juice"
        title = "QRbucks designer"
        choices = ["Caramel Apple Spice", "Steamed Apple Juice"]
        choice = choicebox(msg, title, choices)

        if choice:
            return choice
        else:
            sys.exit(0)

    def drinkSteamers(self):
        msg = "Choose a Steamers"
        title = "QRbucks designer"
        choices = ['pumpkin spice creme', 'cinnamon dolce creme', 'steamed milk', 'vanilla creme']
        choice = choicebox(msg, title, choices)

        if choice:
            return choice
        else:
            sys.exit(0)

    def drinkIcedTeas(self):
        msg = "Choose an Iced Tea"
        title = "QRbucks designer"
        choices = ['iced guava black tea', 'iced guava black tea lemonade', 'iced black tea', \
                   'iced black tea lemonade', 'iced royal english breakfast tea latte', 'iced london fog tea latte', \
                       'iced chai tea latte', 'iced peach green tea', 'iced peach green tea lemonade', \
                           'iced matcha tea latte', 'iced green tea', 'iced green tea lemonade', 'iced matcha lemonade', \
                               'iced passion tango tea', 'iced passion tango tea lemonade']
        choice = choicebox(msg, title, choices)

        if choice:
            return choice
        else:
            sys.exit(0)

    def toppings(self):
         msg = "Choose toppings"
         title = "QRbucks Designer"
         choices = ["Default", "Mocha Drizzle", "Caramel Drizzle",  "Stawberry Drizzle"]
         choice = choicebox(msg, title, choices)

         if choice:
            return choice
         else:
            sys.exit(0)


    def sweetener(self):
        msg = "Choose a sweetener"
        title = "QRbucks Designer"
        choices = ["Default", "None", "Sugar", "Honey", "Stevia in the Raw", "Cane Sugar", \
                   "Sugar in the Raw", "Splenda", "Classic Syrup", "Honey Blend"]
        choice = choicebox(msg, title, choices)

        if choice:
            return choice
        else:
            sys.exit(0)


    def espressoShots(self):
        msg = "Which type of espresso would you like?"
        title = "QRbucks Designer"
        choices = ["Default", "Blonde", "Regular", "Decaf"]
        choice = choicebox(msg, title, choices)

        if choice:
            return choice
        else:
            sys.exit(0)


    def drinkFlavors(self):
        msg = "Choose a Flavor"
        title = "QRbucks designer"
        choices = ["Default", "Apple Brown Sugar",
                   "Brown Sugar", "Caramel", "Cinnamon", "Cinnamon Dolce", \
                   "Funnel Cake" , "Hazelnut", "Peppermint", "Raspeberry", \
               "Toffee Nut", "Vanilla", "Sugar Free Vanilla", "Sauces", \
               "Dark Caramel", "Pumpkin", "White Chocolate Mocha"]
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
            GUI().drinkBuilder()


    def drinkBuilder(self):
        drinkBuilt = ["size", "drink", "drizzle", "espresso", "milk or cream", "syrups"]
        drinkBuilt[0] = GUI().drinkSize()
        currentChoice = GUI().drinkType()
        if currentChoice == "Coffee": #All coffee drinks
            currentChoice = GUI().drinkCoffeeTypes()
            if currentChoice == "Americano":
                drinkBuilt[1] = currentChoice
                drinkBuilt[2] = GUI().toppings()
                drinkBuilt[3] = GUI().espressoShots()
                drinkBuilt[4] = GUI().drinkCream()
                drinkBuilt[5] = GUI().drinkFlavors()
            elif currentChoice == "Brewed Coffees":
                drinkBuilt[1] = GUI().drinkBrewed()
                drinkBuilt[2] = GUI().toppings()
                drinkBuilt[3] = GUI().espressoShots()
                drinkBuilt[4] = GUI().drinkCream()
                drinkBuilt[5] = GUI().drinkFlavors()
            elif currentChoice == "Espresso":
                drinkBuilt[1] = GUI().drinkEspresso()
                drinkBuilt[2] = GUI().toppings()
                drinkBuilt[3] = GUI().espressoShots()
                drinkBuilt[4] = GUI().drinkCream()
                drinkBuilt[5] = GUI().drinkFlavors()
            elif currentChoice == "Iced Coffee":
                drinkBuilt[1] = GUI().drinkIcedCoffee
                drinkBuilt[2] = GUI().toppings()
                drinkBuilt[3] = GUI().espressoShots()
                drinkBuilt[4] = GUI().drinkCream()
                drinkBuilt[5] = GUI().drinkFlavors()
        elif currentChoice == "Hot Drink": #All the hot drinks
            currentChoice = GUI().hotDrinkTypes()
            if currentChoice == "Hot Chocolate":
                drinkBuilt[1] = GUI().drinkHotChocolate()
                drinkBuilt[2] = GUI().toppings()
                drinkBuilt[3] = "None"
                drinkBuilt[4] = GUI().drinkCream()
                drinkBuilt[5] = GUI().drinkFlavors()
            elif currentChoice == "Steamer":
                drinkBuilt[1] = GUI().drinkSteamers()
                drinkBuilt[2] = GUI().toppings()
                drinkBuilt[3] = "None"
                drinkBuilt[4] = GUI().drinkCream()
                drinkBuilt[5] = GUI().drinkFlavors()
            elif currentChoice == "Juice":
                drinkBuilt[1] = GUI().drinkJuice()
                drinkBuilt[2] = GUI().toppings()
                drinkBuilt[3] = "None"
                drinkBuilt[4] = GUI().drinkCream()
                drinkBuilt[5] = GUI().drinkFlavors()
        elif currentChoice == "Cold Drink": #All the cold drinks
            drinkBuilt[1] = GUI().drinkCold()
            drinkBuilt[2] = GUI().toppings()
            drinkBuilt[3] = "None"
            drinkBuilt[4] = GUI().drinkCream()
            drinkBuilt[5] = GUI().drinkFlavors()
        elif currentChoice == "Hot Tea": #All the hot tea
            drinkBuilt[1] = GUI().drinkHotTea()
            drinkBuilt[2] = GUI().toppings()
            drinkBuilt[3] = "None"
            drinkBuilt[4] = GUI().drinkCream()
            drinkBuilt[5] = GUI().drinkFlavors()
        elif currentChoice == "Frappuccino":
            drinkBuilt[1] = GUI().drinkFrappuccino()
            drinkBuilt[2] = GUI().toppings()
            drinkBuilt[3] = GUI().espressoShots()
            drinkBuilt[4] = GUI().drinkCream()
            drinkBuilt[5] = GUI().drinkFlavors()
        elif currentChoice == "Iced Tea": #All the iced tea
            drinkBuilt[1] = GUI().drinkIcedTeas()
            drinkBuilt[2] = GUI().toppings()
            drinkBuilt[3] = "None"
            drinkBuilt[4] = GUI().drinkCream()
            drinkBuilt[5] = GUI().drinkFlavors()
        GUI().confirmChoices()
        return drinkBuilt


    def drinkQRGenerator(self):
        finishedDrink = GUI().drinkBuilder()
        print(finishedDrink)

        img = qrcode.make(str(finishedDrink))
        type(img)
        img.save("Drink.png")


GUI().drinkQRGenerator()
