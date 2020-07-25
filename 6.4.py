class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        self.speed += 10
        print('The car rides')

    def stop(self):
        self.speed = 0
        print('The car stops')

    def turn(self, direction=None):
        print(f'The car terns to the {direction}')

    def show_speed(self):
        print(f'Speed is {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Speed is {self.speed}')
            print('Your speed is too high. Drop it immediately')
        else:
            print(f'Speed is {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Speed is {self.speed}')
            print('Your speed is too high. Drop it immediately')

        else:
            print(f'Speed is {self.speed}')


class PoliceCar(Car):
    pass


my_car = TownCar(40, 'red', 'Lada', False)
my_car.show_speed()
my_car.go()

my_car.show_speed()
my_car.go()
my_car.go()
my_car.show_speed()

print(my_car.is_police)
print(my_car.name)

my_work_car = Car(5, 'black', 'Toyota', False)
print(my_car.color)

my_work_car.go()
my_work_car.show_speed()
