class student:
    def show(self,name,enroll,dept):
        self.name=name
        self.enroll=enroll
        self.dept=dept
        
    def cal(self,mark1,mark2,mark3):
        total=mark1+mark2+mark3
        return total
        
student=student('Marwadi University')
student.show('Vashi',5005,'CS')
