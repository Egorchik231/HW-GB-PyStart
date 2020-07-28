import time


class TrafficLight:
    __colour = ''

    def running(self):
        li = ['red', 'yellow', 'green']

        start_time = time.time()

        while (time.time() - start_time) < 10:
            for i in li:
                TrafficLight.__colour = i
                print(TrafficLight.__colour)
                if TrafficLight.__colour == li[0]:
                    time.sleep(7)
                elif TrafficLight.__colour == li[1]:
                    time.sleep(3)
                elif TrafficLight.__colour == li[2]:
                    time.sleep(5)


crossroads_1 = TrafficLight()
crossroads_1.running()
