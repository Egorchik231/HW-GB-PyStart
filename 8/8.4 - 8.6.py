from 8.3_exceptions import MyEx


class WareHouse:

    def __init__(self, name, location, manager, quantity_places):
        try:
            self.name = name
            self.location = location
            self.manager = manager
            self.quantity_places = quantity_places
            self.income_li = []
            self.outcome_li = []
            if type(quantity_places) != int:
                raise MyEx("quantity_places can't be not int. Try again...")
        except MyEx as mm:
            print(mm)
            quit()


    def acceptance(self, product):
        product.index = len(self.income_li)
        self.income_li.append({'name': product.name, 'quantity': product.quantity})
        self.quantity_places -= product.quantity

    def shipment(self, product, destination):
        self.outcome_li.append(
            {'name': product.name, 'quantity': product.quantity, 'destination_department': destination})
        del self.income_li[product.index]
        self.quantity_places += product.quantity


class OfficeEquipment:
    def __init__(self, name, quantity, color, paperValue, voltage, port_type, wi_fi, usb):

        try:
            self.name = name
            self.quantity = quantity
            self.color = color
            self.paperValue = paperValue
            self.voltage = voltage
            self.port_type = port_type
            self.wi_fi = wi_fi
            self.usb = usb
            self.index = None
            if type(self.quantity) != int or type(self.paperValue) != int or type(self.voltage) != int or type(
                    self.wi_fi) != bool:
                raise MyEx('Your arguments were incorrect. Check it and try again! \n quantity, paperValue and '
                           'voltage must be int. wi_fi must be bool')
        except MyEx as my:
            print(my)
            quit()


class Printer(OfficeEquipment):
    def __init__(self, name, quantity, type_col, color, paperValue, voltage, port_type, wi_fi, usb):
        super().__init__(name, quantity, color, paperValue, voltage, port_type, wi_fi, usb)
        self.type_col = type_col


class Xerox(OfficeEquipment):
    def __init__(self, name, quantity, type_paper, color, paperValue, voltage, port_type, wi_fi, usb):
        super().__init__(name, quantity, color, paperValue, voltage, port_type, wi_fi, usb)
        self.type_paper = type_paper


class Scanner(OfficeEquipment):
    def __init__(self, name, quantity, type_paper, blueTooth, color, paperValue, voltage, port_type, wi_fi, usb):
        super().__init__(name, quantity, color, paperValue, voltage, port_type, wi_fi, usb)
        self.type_paper = type_paper
        self.blueTooth = blueTooth


my_printer = Printer('HP-123', 15, 'RGB', 'black', 500, 12, 'usb-C', True, 3.0)

Moscow_WareHouse = WareHouse('MSK OFFICE ltd', 'Moscow', 'Andrew', 100)
Moscow_WareHouse.acceptance(my_printer)
print(Moscow_WareHouse.income_li)
print(Moscow_WareHouse.quantity_places)

Moscow_WareHouse.shipment(my_printer, 'Head office')
print(Moscow_WareHouse.income_li, '\n', Moscow_WareHouse.outcome_li)


my_printer = Printer('Canon-3', 'asdfgh;', 'RGB', 'black', 500, 12, 'usb-C', True, 3.0)
