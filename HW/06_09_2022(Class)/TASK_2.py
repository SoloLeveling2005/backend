import pickle


class Book:
    def __init__(self, book_title="Три мушкетера", year_of_issue="1844 год", publisher="в парижской газете Le Siècle",
                 genre="литература 19 века, зарубежные приключения, исторические приключения", author="Александр Дюма", price="10000 тг", get=""):
        self.text = None
        self.book_title = book_title  # название книги
        self.year_of_issue = year_of_issue  # год выпуска
        self.publisher = publisher  # издателя
        self.genre = genre  # жанр
        self.author = author  # автора
        self.price = price  # цена
        self.get = get
    # book_title, year_of_issue, publisher, genre, author, price
    def information_on_the_plate(self):
        self.text = (
            "Название книги: ", self.book_title, "Год выпуска: ", self.year_of_issue, "Издатели: ", self.publisher, "Цена: ",
            self.price)
        return self.text

    def detailed_information_on_the_website(self):
        self.text = (
            "Название книги: ", self.book_title, "Год выпуска: ", self.year_of_issue, "Издатели: ", self.publisher, "Цена: ",
            self.price, "Жанр: ", self.genre, "Авторы: ", self.author)
        return self.text

    def get_ser_info(self, get):
        '''
                    Аргументы подаются через пробел
                    Аргументы которые можно подать:
                        book_title \n
                        year_of_issue \n
                        publisher \n
                        genre \n
                        author \n
                        price \n
        '''
        self.get = get.split(" ")

        self.giv_text_info = ""
        for i in self.get:
            # print(i)
            if i == "book_title":
                self.giv_text_info += f"Название книги: {self.book_title} \n"
            elif i == "year_of_issue":
                self.giv_text_info += f"Год выпуска: {self.year_of_issue} \n"
            elif i == "publisher":
                self.giv_text_info += f"Издатели: {self.publisher} \n"
            elif i == "genre":
                self.giv_text_info += f"Жанр: {self.genre} \n"
            elif i == "author":
                self.giv_text_info += f"Авторы: {self.author} \n"
            elif i == "price":
                self.giv_text_info += f"Цена: {self.price} \n"
        return self.giv_text_info
        # print(self.giv_text_info)
        # info_model = pickle.dumps(car.model)
        # info_model_object = pickle.loads(info_model)

    def get_ser_info_car_price(self):
        info_price = pickle.dumps(book.price)
        info_price_object = pickle.loads(info_price)
        return info_price_object
    # def ser_info(self):


# exec
book = Book()
print(book.price)

book = Book(price="12000тг")  # ввод (замена)
print(book.price)  # Вывод

print(book.information_on_the_plate())
print(book.detailed_information_on_the_website())

print(book.get_ser_info("book_title year_of_issue publisher"))
# print(car.get_ser_info())

print(book.get_ser_info_car_price())