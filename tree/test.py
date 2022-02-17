class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        # self.info = f"{self.name} has got {self.marks}"

    def change_marks(self, new_marks):
        self.marks = new_marks

    @property
    def show_marks(self):
        print(f"changed self.marks = {self.marks} ")


# creating object of Student class
st_1 = Student("Max", 80)


def p():
    print(
        f"self.name = {st_1.name}\nself.marks = {st_1.marks}\n")


p()
st_1.marks = 85
# p()
st_1.change_marks(86)
# p()
st_1.show_marks()
