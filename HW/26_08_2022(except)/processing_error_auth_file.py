import time
from pprint import pprint
import sys


animation = ["■□□□□□□□□□", "■■□□□□□□□□", "■■■□□□□□□□", "■■■■□□□□□□", "■■■■■□□□□□", "■■■■■■□□□□", "■■■■■■■□□□",
             "■■■■■■■■□□", "■■■■■■■■■□", "■■■■■■■■■■", "Обработка завершена \n"]
request_keys_default = ["url", "method", "data", "timeout", "headers"]
methods_default = ["GET", "POST", "PUT", "DELETE", "AUTH", "HEAD", "PATCH"]


def processing_error_auth(func):
    def excepted(request_data, time_sleep=0.5, check_request_keys=True, check_methods=True,
                 request_keys=request_keys_default, methods=methods_default):

        print("Начинаю обработку")
        for i in range(len(animation)):
            time.sleep(time_sleep)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()

        if len(request_data) == 0:
            print("Возникла ошибка")
            time.sleep(.2)
            raise KeyError('Подан пустой словарь')

        if check_request_keys:
            if len(request_data) < 5:
                print("Отсутсвуют элементы с ключем:")
                for i in request_keys:
                    if request_data.get(i, None):
                        pass
                    else:
                        print(i)
        else:
            print("Проверка ключа отключена")

        if check_methods:
            try:
                if request_data["method"] not in methods:
                    request_data_except = request_data["method"]
                    raise NonExistentMethod(error=request_data_except)
            except KeyError:
                pass
        else:
            print("Проверка метода отключена")

        result = func(request_data)

        return result

    return excepted


class AuthError:
    @processing_error_auth
    def auth_error(self):  # request_data_1
        # Обработка полученного словаря (request запроса)
        # Ели словарь пустой вызов @processing_error_auth

        print("Ваш словарь: ")
        pprint(self)


class NonExistentMethod(Exception):

    def __init__(self, error, ):
        self.message = f"Метод '{error}' не существует"

        super().__init__(self.message)

