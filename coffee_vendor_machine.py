#input:c
#input:2
#output:enjoy your! Cappuccino Coffee


Coffee = {
    1: "Espresso Coffee",
    2: "Cappuccino Coffee",
    3: "Latte Coffee",
}
Tea = {
    1: "Plain Tea",
    2: "Assam Tea",
    3: "Ginger Tea",
    4: "CardamomTea",
    5: "Masala Tea",
    6: "Lemon Tea",
    7: "Green Tea",
    8: "Organic Darjeeling Tea",
    9: "Soups Tea",
}
Soups = {
    1: "Hot and Sour",
    2: "Veg Corn Soup",
    3: "Tomato Soup",
    4: "Spicy Tomato Soup",
}
Beverages = {
    1: "Hot Chocolate Drink",
    2: "Badam Drink",
    3: "Badam-Pista Drink",

}

ch = 'ctsb'
a = input()
if a in ch:
    n = int(input())
    if a == 'c':
        dict1 = Coffee
    elif a == 't':
        dict1 = Tea
    elif a == 's':
        dict1 = Soups
    elif a == 'b':
        dict1 = Beverages

    try:
        print("Enjoy your", dict1[n])
    except:
        print("INVALID OUTPUT!")
else:
    print("INVALID OUTPUT!")
