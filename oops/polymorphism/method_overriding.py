class Bird:
    def fly(self):
        print("Birds can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly")

b = Bird()
p = Penguin()

b.fly()  # Birds can fly
p.fly()  # Penguins cannot fly
