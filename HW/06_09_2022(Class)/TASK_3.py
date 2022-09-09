import pickle


class Stadium:
    def __init__(self, stadium_name="Уэмбли", opening_date="2007 год", country="Великобритания",
                 city="Лондон", capacity="90 000", get=""):
        self.text = None
        self.stadium_name = stadium_name  # название стадиона
        self.opening_date = opening_date  # дату открытия
        self.country = country  # страну
        self.city = city  # город
        self.capacity = capacity  # вместимость
        self.get = get
    # stadium_name, opening_date, country, city, capacity
    # название стадиона, дату открытия, страну, город, вместимость
    # brief_information. full_information
    def brief_information(self):
        self.text = (
            "Название стадиона: ", self.stadium_name, "Дата открытия: ", self.opening_date, "Страна: ", self.country, "Город: ",
            self.city)
        return self.text

    def full_information(self):
        self.text = (
            "Название стадиона: ", self.stadium_name, "Дата открытия: ", self.opening_date, "Страна: ", self.country, "Город: ",
            self.city, "Вместимость: ", self.capacity)
        return self.text

    def get_ser_info(self, get):
        '''
                    Аргументы подаются через пробел
                    Аргументы которые можно подать:
                        stadium_name \n
                        opening_date \n
                        country \n
                        city \n
                        capacity \n
        '''
        self.get = get.split(" ")

        self.giv_text_info = ""
        for i in self.get:
            # print(i)
            if i == "stadium_name":
                self.giv_text_info += f"Название стадиона: {self.stadium_name} \n"
            elif i == "opening_date":
                self.giv_text_info += f"Дата открытия: {self.opening_date} \n"
            elif i == "country":
                self.giv_text_info += f"Страна: {self.country} \n"
            elif i == "city":
                self.giv_text_info += f"Город: {self.city} \n"
            elif i == "capacity":
                self.giv_text_info += f"Вместимость: {self.capacity} \n"
        return self.giv_text_info
        # print(self.giv_text_info)
        # info_model = pickle.dumps(car.model)
        # info_model_object = pickle.loads(info_model)

    # def ser_info(self):


# exec
stadium = Stadium()
print(stadium.capacity)

stadium = Stadium(capacity="1200000")  # ввод (замена)
print(stadium.capacity)  # Вывод

print(stadium.brief_information())
print(stadium.full_information())

print(stadium.get_ser_info("stadium_name opening_date country"))
# print(car.get_ser_info())

"""




#Задание 1 
Реализуйте класс «Автомобиль». Необходимо хранить в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса. 
#Задание 4 
Реализуйте класс «Автомобиль». Необходимо хранить в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

#Задание 2 
Реализуйте класс «Книга». Необходимо хранить в полях класса: название книги, год выпуска, издателя, жанр, автора, цену. Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса. 
#Задание 5 
Реализуйте класс «Книга». Необходимо хранить в полях класса: название книги, год выпуска, издателя, жанр, автора, цену. Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

#Задание 3 
Реализуйте класс «Стадион». Необходимо хранить в полях класса: название стадиона, дату открытия, страну, город, вместимость. Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
Задание 6 
Реализуйте класс «Стадион». Необходимо хранить в полях класса: название стадиона, дату открытия, страну, город, вместимость. Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.



"""