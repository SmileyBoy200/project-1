import random
response = "y"
while response=="y":
    no = random.randint(1,6)
    print(no)
    response=input("press y to roll again and press n to exit")
