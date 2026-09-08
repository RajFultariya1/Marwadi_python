class university:
    def __init__(self,university_name):
        self.university_name=university_name
    class student:
        def __init__(self,name,Enroll,dept):
            self.name=name
            self.Enroll=Enroll
            self.dept=dept
        
        def show(self):
            print("Name is : ",self.name)
            print("Enroll is : ",self.Enroll)
            print("Dept is : ",self.dept)

uni=university('Marwadi University')
ob1=uni.student('vashi',5005,'CS')
ob1.show()
