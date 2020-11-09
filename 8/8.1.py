class Date:
    day = None
    month = None
    year = None

    def __init__(self, date):
        self.date = date


    def assist(self):
        return self.date


    @classmethod
    def to_int(cls):
        da_li = cls.assist(Date('40-20-2020')).split(sep='-')
        cls.day = int(da_li[0])
        cls.month = int(da_li[1])
        cls.year = int(da_li[2])


    @staticmethod
    def check_method():

        if Date.day > 31 or Date.day < 1:
            print('Day is not correct')
        if 1 > Date.month or Date.month > 12:
            print('Month is not correct')
        if 1 > Date.year or Date.year > 2020:
            print('Year is not correct')


Date.to_int()
Date.check_method()
