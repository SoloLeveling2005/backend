class Car_dollar:
    def __init__(self, model="Toyota RAV4", year_of_manufacture="1994 год", manufacturer="Toyota Motor Corporation",
                 engine_capacity="от 1.8 до 3.5 л.", color="black", price="4 000 000$", get=""):
        self.text = None
        self.model = model  # название модели
        self.year_of_manufacture = year_of_manufacture  # год выпуска
        self.manufacturer = manufacturer  # производителя
        self.engine_capacity = engine_capacity  # объем двигателя
        self.color = color  # цвет машины
        self.price = price  # цена
        self.get = get
    def one(self):
        return self.model

class Car_tenge:
    def __init__(self, model="Toyota RAV4", year_of_manufacture="1994 год", manufacturer="Toyota Motor Corporation",
                 engine_capacity="от 1.8 до 3.5 л.", color="white", price="16 293 500 тг", get=""):
        self.text = None
        self.model = model  # название модели
        self.year_of_manufacture = year_of_manufacture  # год выпуска
        self.manufacturer = manufacturer  # производителя
        self.engine_capacity = engine_capacity  # объем двигателя
        self.color = color  # цвет машины
        self.price = price  # цена
        self.get = get
    def one(self):
        return self.model

class Multi(Car_dollar, Car_tenge):
    def __init__(self):
        super().__init__()
        self.car_dollar = Car_dollar()
        self.car_tenge = Car_tenge()
    def compare(self):
        text = f"{self.car_dollar.model} <=> {self.car_tenge.model} \n{self.car_dollar.year_of_manufacture} <=> {self.car_tenge.year_of_manufacture} \n{self.car_dollar.manufacturer} <=> {self.car_tenge.manufacturer} \n{self.car_dollar.engine_capacity} <=> {self.car_tenge.engine_capacity} \n{self.car_dollar.color} <=> {self.car_tenge.color} \n{self.car_dollar.price} <=> {self.car_tenge.price} "
        print(text)



a = Multi()
a.compare()