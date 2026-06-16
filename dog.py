class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"O {self.name} sentou")

    def roll_over(self):
        print(f"O {self.name} rolou")

meu_cachorro = Dog("Jurandir" ,7)
meu_cachorro.sit()
meu_cachorro.roll_over()


