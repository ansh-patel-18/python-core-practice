class room:
    standard = 10
    school = "sahajanand"
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
std_1 = room("Ansh",1)
print(f"Name : {std_1.name}\nRollNo. : {std_1.rollno}\nStandard : {std_1.standard}\nSchool : {std_1.school}")
