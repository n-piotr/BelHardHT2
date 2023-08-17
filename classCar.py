class Car:
    def __init__(self, marka, model, price, power):
        self.marka = marka
        self.model = model
        self.price = price
        self.power = power  # self.__power = power = private

    def get_marka(self):
        return self.marka

    def set_marka(self, marka):
        self.marka = marka

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_price(self,):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_power(self):
        return self.power

    def set_power(self, power):
        self.power = power

    def __str__(self):
        return f"{self.marka} {self.model} {self.price} {self.power}"
