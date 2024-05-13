class student_details:
    def __init__(self):
        self.name = input("Enter your Name :")
        self.reg_no = input("Enter your Regno :")
        self.college = input('Enter the Colege :')

class Student(student_details):
    def access(self):
        print('\nName:', self.name)

        if self.reg_no[2:5].upper() == 'BAM':
            print('Code:', self.reg_no[2:5])
            self.department = 'AIML'
            print('Department :', self.department)
            self.course = 'Artificial Intelligence & Machine Learning'
            print('Course Name :', self.course)

        elif self.reg_no[2:5].upper() == 'BDA':
            print('Code:', self.reg_no[2:5])
            self.department = 'DSA'
            print('Department :', self.department)
            self.course = 'Data Science & Analytics'
            print('Course Name :', self.course)

        elif self.reg_no[2:5].upper() == 'BFS':
            print('Code:', self.reg_no[2:5])
            self.department = 'BCFS'
            print('Department :', self.department)
            self.course = 'Cyber Security & Forensics Science'
            print('Course Name :', self.course)

        
        elif self.reg_no[2:5].upper() == 'BCS':
            print('Code:', self.reg_no[2:5])
            self.department = 'BCS'
            print('Department :', self.department)
            self.course = 'Computer Science'
            print('Course Name :', self.course)

        
        elif self.reg_no[2:5].upper() == 'BCA':
            print('Code:', self.reg_no[2:5])
            self.department = 'BCA'
            print('Department :', self.department)
            self.course = 'Computer Application'
            print('Course Name :', self.course)



        if self.department.upper() == 'AIML':
            self.branch = 'Computer Science'
            print('Branch :', self.branch)

        elif self.department.upper() == 'DSA':
            self.branch = 'Computer Science'
            print('Branch :', self.branch)

        elif self.department.upper() == 'BCFS':
            self.branch = 'Computer Science'
            print('Branch :', self.branch)

        elif self.department.upper() == 'BCA':
            self.branch = 'Computer Science'
            print('Branch :', self.branch)

        elif self.department.upper() == 'BCS':
            self.branch = 'Computer Science'
            print('Branch :', self.branch)



        if self.branch == 'Computer Science':
            self.director = 'Tom Cruise'
            print('Director :', self.director)



        if self.college.upper() == 'STC':
            self.university = 'Bharathiyar University'
            print('College:', self.college)
            print('University:', self.university)


std = Student()
std.access()
