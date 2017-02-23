class Mine():
    myAge=45#global variable
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def run(self):
        print(self.name)
        print(self.age)

m=Mine('Oshy', 22)
m.run()
