class Computer:

    def __init__(self):
        self.__maxprice = 600
        # print ("From constructor",self.__maxprice)


    def sell(self):
        print ("Selling Price is {} from sell method".format(self.__maxprice))

    def setmaxprice(self,price):
        self.__maxprice=price
        # print ("it is set {} from sell method".format(self.__maxprice))



c = Computer()
c.sell()

c.__maxprice=100
c.sell()


c.setmaxprice(900)
c.sell()


