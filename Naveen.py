
class Pycharm:

    def execute(self):
        print('Compiling')
        print('Running')


class MyEditor:

    def execute(self):
        print('Spell checking')
        print('Convention check')
        print('Compiling')
        print('Running')


class Laptop:

    def code(self, ide):
        ide.execute()


ide = MyEditor()
l1 = Laptop()
l1.code(ide)
