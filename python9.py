class student_details:
    def __init__(self):
        self.name = input("Enter your Name :")
        self.reg_no = input("Enter your Regno :")
        self.college = input('Enter the Colege :')

class student(student_details):
    def access(self):
        print('\n')
        print('Name :',self.name)
                
        if self.reg_no[2:5] == 'BAM' or 'bam' or 'Bam':
            print('Code :' , self.reg_no[2:5])
            self.department = 'AIML'
            self.course = 'Artificial INtelligence & Machine Leanring'
            print('Reg.No :',self.reg_no)
            print('Department :' , self.department)
            print('Course Name :' , self.course)

        elif self.reg_no[2:5] == 'BDA' or 'bda' or 'Bda':
            print('Code :' , self.reg_no[2:5])
            self.department = 'DSA'
            self.course = 'Data Science & Analytics'
            print('Reg.No :',self.reg_no)
            print('Department :' , self.department)
            print('Course Name :' , self.course)

        elif self.reg_no[2:5] == 'BFS' or 'bfs' or 'Bfs':
            print('Code :' , self.reg_no[2:5])
            self.department = 'BCFS'
            self.course = 'Cyber Security & Forensics Science'
            print('Reg.No :',self.reg_no)
            print('Department :' , self.department)
            print('Course Name :' , self.course )

        
        if self.department == 'AIML' or 'Aiml' or 'aiml':
            self.branch = 'Computer Science'
            print('Branch :' , self.branch)

        elif self.department == 'DSA':
            self.branch = 'Computer Science'
            print('Branch :' , self.branch)

        elif self.department == 'BCFS':
            self.branch = 'Computer Science'
            print('Branch :' , self.branch)


        if self.branch == 'Computer Science':
            self.director = 'Tom Curise'
            print('Director :' , self.director)

        if self.college == 'STC' or 'stc':
            self.university = 'Bharathiyar University'
            print('College :' , self.college)
            print('University :',self.university)

std = student()
std.access()
