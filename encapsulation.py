# class toys:
#     def __init__(self):
#         self.__price=200
#     def printPrice(self):
#         print(self.__price)
#     def changePrice(self,updatedvalue):
#         self.__price=updatedvalue

# object=toys()
# object.printPrice()

# object.changePrice(300)
# object.printPrice()

class books:
    def __init__(self):
        self.__sellprice=350
    def printsellprice(self):
        print(self.__sellprice)

    def changesellprice(self,newvalue):
        self.__sellprice=newvalue

ob=books()
ob.changesellprice(300)
ob.printsellprice()