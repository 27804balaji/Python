class student_details:
    def _details(self): # Protected Function
        self.name = input("Enter your Name :")
        self.__reg_no = input("Enter your Regno :") # Private Variable
        self.department = input("Enter your Department :")
class student(student_details):
    def access(self):
        student_details._details(self)
        
std = student_details()
std._details()
