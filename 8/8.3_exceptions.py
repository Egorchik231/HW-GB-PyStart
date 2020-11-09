class MyEx (Exception):
    def __init__(self, txt):
        self.txt = txt


if __name__ == '__main__':
    my_li = []
    while True:

        a = input('Enter el to put it to list: ')
        if a == 'stop':
            break
        try:
            my_li.append(int(a))

        except ValueError:
            print(MyEx('Please enter numbers only!'))

        except MyEx as my:
            print(my)
            continue

    print(my_li)