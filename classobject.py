class Parrot:
    species = "Bird"

    def __init__(self,name,age):
        self.name = name
        self.age = age


blue = Parrot("BLu",10)
woo =  Parrot("Woo",20)

print("Blue is a {}".format(blue.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))


print("{} is {} year old".format(blue.name,blue.age))
print("{} is {} year old".format(woo.name,woo.age))