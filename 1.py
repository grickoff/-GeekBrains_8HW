# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Data:

    def __init__(self, input_str):
        self.input_str = input_str

    @classmethod
    def convert(cls, input_str):
        return tuple(map(int, input_str.split('-')))

    @staticmethod
    def validate(date):
        if date[0] <= 0 or date[0] > 31:
            return

        if date[1] <= 0 or date[1] > 12:
            return

        if len(str(date[2])) != 4:
            return

        return print('валидация прошла успешно')

dm = Data('01-12-2002')
print(Data. convert(dm.input_str))
Data.validate(Data. convert(dm.input_str))




       # return print(True)
    # def month(Data.convert):
    #     if Data.convert[2] in range(1, 12):
    #         print(True)


