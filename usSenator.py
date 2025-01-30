print("US House of Representatives and Senates")
print("==========================================")

age=int(input("enter ur age  "))
years=int(input("how many years did u live in us?  "))

if(years >= 9 and age >= 30):
    print("you are eligible to be US senator")
elif(years >= 7 and age >= 25):
    print("you are eligible to be US Representative")
else:
    print("deport this mf")