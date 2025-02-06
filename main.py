"""
Buyer -> location, name, city, country, coordinates

some kind of product class
Product ->
Warehouse -> product, country, coordinates x and y, stock (quantity)
"""
import math


class Buyer:
    def __init__(self, name, city, country, coordinates, product, quantity):
        self.name = name
        self.city = city
        self.country = country
        self.coordinates = coordinates
        self.product = product
        self.quantity = quantity

class Product:
    def __init__(self, name, warehouse):
        self.name = name
        self.warehouses = warehouse

class Warehouse:
    def __init__(self, city, country, coordinates, stock):
        self.city = city
        self.country = country
        self.coordinates = coordinates
        self.stock = stock

class DeliveryStrategy:
    def __init__(self, buyer):
        self.buyer = buyer

    def stockAvailability(self):
        quantityFromBuyer = self.buyer.quantity
        availableWarehouses = []
        for warehouse in list(self.buyer.product.warehouses.values()):
            if warehouse.stock >= quantityFromBuyer:
                availableWarehouses.append(warehouse.city)
            else:
                self.buyer.product.warehouses.pop(warehouse.city)
        print(self.buyer.product.warehouses.keys())
        return availableWarehouses

    def shipWithinCountry(self, buyer, product, availableList):
        availableWarehouses = []
        for warehouse in product.warehouses.values():
            if warehouse.country == buyer.country:
                availableWarehouses.append(warehouse.city)
        return availableWarehouses

    def closestToBuyer(self, buyer, product):
        minDistance = ["random", 99999]
        for warehouse in product.warehouses.values():
            warehouseCoords = warehouse.coordinates
            buyerCoords = buyer.coordinates
            xCoordDiff = buyerCoords[0] - warehouseCoords[0]
            yCoordDiff = buyerCoords[1] - warehouseCoords[1]
            squareFirst = math.pow(xCoordDiff, 2)
            squareSecond = math.pow(yCoordDiff, 2)
            distance = math.sqrt(math.pow(warehouseCoords[0], 2) + math.pow(warehouseCoords[1], 2))
            distance = math.sqrt(squareFirst + squareSecond)
            if distance < minDistance[1]:
                minDistance = [warehouse.city, distance]
        return product.warehouses[minDistance[0]].city


if __name__ == '__main__':
    warehouse1 = Warehouse("Toronto", "Canada", [2,2], 1)
    warehouse2 = Warehouse("Montreal", "Canada", [3,-1], 99)
    warehouse3 = Warehouse("Seattle", "US", [-2,1], 5)
    warehouse4 = Warehouse("London","UK", [10,3], 10)
    laptop = Product("laptop", {"Toronto" : warehouse1, "Montreal" : warehouse2, "Seattle" : warehouse3, "London" : warehouse4})
    Tom = Buyer("Tom", "Vancouver", "Canada", [-2,5], laptop, 5)
    Jack = Buyer("Jack", "Paris", "France", [15, -3], laptop, 100)
    deliveryStrategy = DeliveryStrategy(Jack)
    print(deliveryStrategy.stockAvailability())

