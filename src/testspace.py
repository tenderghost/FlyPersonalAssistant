from .dog import Dog

class ZangAo(Dog):
    def __init__(self):
        super().__init__("little_zangao", 12)

    def spark(self):
        print("Wo wo wo!")

my_dog = Dog('Puppy', 3)
my_dog.spark()

zangao = ZangAo()
zangao.spark()

