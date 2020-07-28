class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print('Full income equal:', self._income['wage'] + self._income['bonus'])


pers_1 = Position('Egor', 'Filippov', 'Manager', 10000, 5000)
pers_1.get_full_name()
pers_1.get_total_income()
