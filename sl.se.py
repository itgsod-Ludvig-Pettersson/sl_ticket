def fares(age,barn=False, senior=False, vuxen=False):
    if age>=20 and age>20 and age<=65:
        if barn==True:
            return"price is 25kr"
        elif senior==True:
            return"price is 25kr"
        else:
            return"price is 50kr"
    elif age <20 or age >65:
        if barn==True:
            return"price is 25kr"
        elif senior==True:
            return"price is 25kr"
        elif barn==True:
            return "price is 25kr"
        else:
            return"price is 25kr"

print fares(65,senior=True)
print fares(40,vuxen=False)
print fares(15,barn=True)



