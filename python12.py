class I_year:
    def __init__(self):
        self.name = input('Enter the Name :')
        self.__reg_no = input('Enter the Reg.No :')
            
    def department(self):
        if self.__reg_no[2:5].upper() == 'BAM':
            self.department = 'AIML' 
            print('Department :' , self.department)


std = I_year()
std.department()