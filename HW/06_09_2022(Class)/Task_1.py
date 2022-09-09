import pickle


class Car:
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

    def information_on_the_plate_in_the_car_dealership(self):
        self.text = (
            "Модель: ", self.model, "Год выпуска: ", self.year_of_manufacture, "Цвет двигателя: ", self.color, "Цена: ",
            self.price)
        return self.text

    def detailed_information_on_the_website(self):
        self.text = (
            "Модель: ", self.model, "Год выпуска: ", self.year_of_manufacture, "Цвет двигателя: ", self.color, "Цена: ",
            self.price, "Производитель: ", self.manufacturer, "Объем двигателя: ", self.engine_capacity)
        return self.text

    def get_ser_info(self, get):
        '''
                    Аргументы подаются через пробел
                    Аргументы которые можно подать:
                        model \n
                        year_of_manufacture \n
                        manufacturer \n
                        engine_capacity \n
                        color \n
                        price \n
        '''
        self.get = get.split(" ")

        self.giv_text_info = ""
        for i in self.get:
            # print(i)
            if i == "model":
                self.giv_text_info += f"Модель: {self.model} \n"
            elif i == "year_of_manufacture":
                self.giv_text_info += f"Год выпуска: {self.year_of_manufacture} \n"
            elif i == "manufacturer":
                self.giv_text_info += f"Производитель: {self.manufacturer} \n"
            elif i == "engine_capacity":
                self.giv_text_info += f"Объем двигателя: {self.engine_capacity} \n"
            elif i == "color":
                self.giv_text_info += f"Цвет: {self.color} \n"
            elif i == "price":
                self.giv_text_info += f"Цена: {self.price} \n"
        return self.giv_text_info
        # print(self.giv_text_info)
        # info_model = pickle.dumps(car.model)
        # info_model_object = pickle.loads(info_model)

    def get_ser_info_car_price(self):
        info_price = pickle.dumps(car.price)
        info_price_object = pickle.loads(info_price)
        return info_price_object

    def ser_info(self,information_on_the_plate_in_the_car_dealership,detailed_information_on_the_website):
        a = information_on_the_plate_in_the_car_dealership()
        return a


# exec
car = Car()
print(car.price)

car = Car(price="120000000тг")  # ввод (замена)
print(car.price)  # Вывод

print(car.information_on_the_plate_in_the_car_dealership())
print(car.detailed_information_on_the_website())

print(car.get_ser_info("model color price"))
# print(car.get_ser_info())

print(car.get_ser_info_car_price())


print(car.ser_info)



