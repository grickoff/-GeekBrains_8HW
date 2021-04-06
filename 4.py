#  Начните работу над проектом «Склад оргтехники».
#  Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
#  Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
#  В базовом классе определить параметры, общие для приведенных типов.
#  В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Stock:


    def shelf(self):
        return print('Полка склада')


class Equipment(Stock):

    def __init__(self, name, serial_number):
        self.name = name
        self.serial_number = serial_number

class Printer(Equipment):

    def printing(self):
        print(self.name, self.serial_number, '...doing printing...')

class Scanner(Equipment):

    def do_scan(self):
        print(self.name, self.serial_number, '...doing scanning...')

class Xerx(Equipment):

    def persian_king(self):
        print('Ксеркс I (др.-перс. 𐎧𐏁𐎹𐎠𐎼𐏁𐎠 Xšayāršā, '
                            'что означает «Царь героев» или «Герой среди царей»)' '\n'
              ' Сын Дария I и Атоссы, дочери Кира II - начинает военный поход')

first_thing = Printer('принтер', 123)
first_thing.printing()

second_thing = Scanner('сканер', 345)
second_thing.do_scan()

third_thing = Xerx('Ксеркс', 'I')
third_thing.persian_king()


