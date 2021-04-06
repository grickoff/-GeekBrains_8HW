#  Продолжить работу над первым заданием.
#  Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
#  Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
#  можно использовать любую подходящую структуру, например словарь.

printer_list = []
scanner_list = []
xerx_list = []

class Stock:

    def add_scanner(self):
        scanner_list.append(f'{self.name} - {self.serial_number}')
        print(scanner_list)

    def add_printer(self):
        printer_list.append(f'{self.name} - {self.serial_number}')
        print(printer_list)

    def add_xerx(self):
        xerx_list.append(f'{self.name} - {self.serial_number}')
        print(xerx_list)




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

first_thing = Printer('принтер', 111)
first_thing.add_printer()
first_thing.printing()

second_thing = Scanner('сканер', 111)
second_thing.add_scanner()
second_thing.do_scan()

third_thing = Xerx('Ксеркс', 'I')
third_thing.add_xerx()
third_thing.persian_king()

print(printer_list)
print(scanner_list)
print(xerx_list)



