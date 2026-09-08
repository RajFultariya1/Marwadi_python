class Student:

    university = "Marwadi"

    def __init__(self,name,enroll,marks):
        self.name = name
        self.enroll = enroll
        self.marks = marks

    def show(self):
        print("student name",self.name)
        print("enoll",self.enroll)
        print("marks",self.marks)

    def display(cls):
        if marks<=40:
            return 'pass'
        else:
            return 'fail'

stud=student('vashi',5005,89)
