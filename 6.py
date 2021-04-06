# Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

printer_list = []
scanner_list = []
xerx_list = []


class Stock:

    def add_scanner(self):
        scanner_list.append(f'{self.name} - {self.serial_number}')


    def add_printer(self):
        printer_list.append(f'{self.name} - {self.serial_number}')


    def add_xerx(self):
        xerx_list.append(f'{self.name} - {self.serial_number}')





class Equipment(Stock):

    def __init__(self, name, serial_number):
        self.name = name
        self.serial_number = serial_number
        while True:
            try:
                self.serial_number != int(self.serial_number)
            except ValueError:
                    print('Не верный тип данных. вводить только цифры')
                    self.serial_number = input(f'введите серийный номер {self.name} ')
            else:
                break



class Printer(Equipment):

    def printing(self):
        print(self.shelf(), self.name, self.serial_number, '...doing printing...')

class Scanner(Equipment):

    def do_scan(self):
        print(self.shelf(), self.name, self.serial_number, '...doing scanning...')

class Xerx(Equipment):

    def persian_king(self):
        print(self.shelf(), 'Ксеркс I (др.-перс. 𐎧𐏁𐎹𐎠𐎼𐏁𐎠 Xšayāršā, '
                            'что означает «Царь героев» или «Герой среди царей»)' '\n'
              ' Сын Дария I и Атоссы, дочери Кира II - начинает военный поход')

first_thing = Printer('принтер', 111)
first_thing.add_printer()

new_printer = Printer(input('название принтера '), input('серийный номер принтера '))
new_printer.add_printer()
print(new_printer.shelf())
print(f'список принтеров на складе: {printer_list}')



