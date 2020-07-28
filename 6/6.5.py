class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen (Stationary):
    def draw(self):
        print('Pen drawing')


class Pencil (Stationary):
    def draw(self):
        print('Pencil drawing')


class Handle (Stationary):
    def draw(self):
        print('Handle drawing')


pen = Pen('pen')
pen.draw()

pencil = Pencil('pencil')
pencil.draw()

handle = Handle('handle')
handle.draw()