class calculator:
    def __init__(self, n):
        self.n = n

    def square (self):
        print(f"The square is {self.n*self.n}")
p = int(input("Enter any number : "))
p=calculator(p)
p.square()