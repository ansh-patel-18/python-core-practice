class Student:
    def __init__(self, name:str, age: int):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, text: str):
        name, age = text.split("-")
        return cls(name, int(age))

if __name__ == "__main__":
    s1 = Student("Rahul", 20)
    print(f"Normal: {s1.name}, Age : {s1.age}")

    s2 = Student.from_string("Ansh-22")
    print(f"From String: {s2.name}, Age : {s2.age}")