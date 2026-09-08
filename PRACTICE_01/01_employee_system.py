class employee:
    language = "JavaScript"
    salary = 1200000
      
    def __init__(self, name, salary, language): # dunder method which is autometically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
    
    def getinfo(self, age, collage):
        self.age = age
        self.language = collage
        print(f"\nThe language is {self.language}. the salary is {self.salary}.")
    @staticmethod
    def data():
        print("\nGood morning")
    
ansh = employee("Ansh patel", 1500000, "Python")
print(ansh.name, ansh.language, ansh.salary)

ansh.getinfo()
ansh.data()

###############################################################################

class data:
    def __init__(self, name, age, collage, salary, birthplace):
        self.name = name
        self.age = age
        self.collage = collage
        self.salary = salary
        self.birthplace = birthplace
info = data("Ansh Patel", 22, "Monark", 150000, 'Ahmedabad')
print(f"Name \t: {info.name}\nAge \t: {info.age}\nCollage : {info.collage}")
