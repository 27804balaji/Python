class I_year:
    def __init__(self):
        self.name = input('Enter the Name :')
        self.__reg_no = input('Enter the Reg.No :')
        
class II_year:
    def __init__(self):
        self.name = input('Enter the Name :')
        self.__reg_no = input('Enter the Reg.No :')
        
class III_year:
    def __init__(self):
        self.name = input('Enter the Name :')
        self.__reg_no = input('Enter the Reg.No :')
        

class College_I(I_year):
    def __department(self):
        print('\n')
        print('Name :' , self.name)
        print('Reg.No :' , self._I_year__reg_no)

        if self._I_year__reg_no[2:5].upper() == 'BAM': 
            print('Code:', self._I_year__reg_no[2:5])
            self.department = 'AIML' 
            print('Department :' , self.department)
            self.course = 'Data Science & Analytics'
            print('Course Name :', self.course)

        elif self._I_year__reg_no[2:5].upper() == 'BDA':
            print('Code:', self._I_year__reg_no[2:5])
            self.department = 'DSA'
            print('Department :', self.department)
            self.course = 'Data Science & Analytics'
            print('Course Name :', self.course)

        elif self._I_year__reg_no[2:5].upper() == 'BFS':
            print('Code:', self._I_year__reg_no[2:5])
            self.department = 'BCFS'
            print('Department :', self.department)
            self.course = 'Cyber Security & Forensics Science'
            print('Course Name :', self.course)        
        elif self._I_year__reg_no[2:5].upper() == 'BCS':
            print('Code:', self._I_year__reg_no[2:5])
            self.department = 'BCS'
            print('Department :', self.department)
            self.course = 'Computer Science'
            print('Course Name :', self.course)

        
        elif self._I_year__reg_no[2:5].upper() == 'BCA':
            print('Code:', self._I_year__reg_no[2:5])
            self.department = 'BCA'
            print('Department :', self.department)
            self.course = 'Computer Application'
            print('Course Name :', self.course)


class College_II(II_year):
    def __department(self):
        print('\n')
        print('Name :' , self.name)
        print('Reg.No :' , self._I_year__reg_no)

        if self._II_year__reg_no[2:5].upper() == 'BAM': 
            print('Code:', self._II_year__reg_no[2:5])
            self.department = 'AIML' 
            print('Department :' , self.department)
            self.course = 'Data Science & Analytics'
            print('Course Name :', self.course)

        elif self._II_year__reg_no[2:5].upper() == 'BDA':
            print('Code:', self._II_year__reg_no[2:5])
            self.department = 'DSA'
            print('Department :', self.department)
            self.course = 'Data Science & Analytics'
            print('Course Name :', self.course)

        elif self._II_year__reg_no[2:5].upper() == 'BFS':
            print('Code:', self._II_year__reg_no[2:5])
            self.department = 'BCFS'
            print('Department :', self.department)
            self.course = 'Cyber Security & Forensics Science'
            print('Course Name :', self.course)

        
        elif self._II_year__reg_no[2:5].upper() == 'BCS':
            print('Code:', self._II_year__reg_no[2:5])
            self.department = 'BCS'
            print('Department :', self.department)
            self.course = 'Computer Science'
            print('Course Name :', self.course)

        
        elif self._II_year__reg_no[2:5].upper() == 'BCA':
            print('Code:', self._II_year__reg_no[2:5])
            self.department = 'BCA'
            print('Department :', self.department)
            self.course = 'Computer Application'
            print('Course Name :', self.course)


class College_III(III_year):
    def __department(self):
        print('\n')
        print('Name :' , self.name)
        print('Reg.No :' , self._I_year__reg_no)

        if self._III_year__reg_no[2:5].upper() == 'BAM': 
            print('Code:', self._III_year__reg_no[2:5])
            self.department = 'AIML' 
            print('Department :' , self.department)
            self.course = 'Data Science & Analytics'
            print('Course Name :', self.course)

        elif self._III_year__reg_no[2:5].upper() == 'BDA':
            print('Code:', self._III_year__reg_no[2:5])
            self.department = 'DSA'
            print('Department :', self.department)
            self.course = 'Data Science & Analytics'
            print('Course Name :', self.course)

        elif self._III_year__reg_no[2:5].upper() == 'BFS':
            print('Code:', self._III_year__reg_no[2:5])
            self.department = 'BCFS'
            print('Department :', self.department)
            self.course = 'Cyber Security & Forensics Science'
            print('Course Name :', self.course)

        
        elif self._III_year__reg_no[2:5].upper() == 'BCS':
            print('Code:', self._III_year__reg_no[2:5])
            self.department = 'BCS'
            print('Department :', self.department)
            self.course = 'Computer Science'
            print('Course Name :', self.course)

        
        elif self._III_year__reg_no[2:5].upper() == 'BCA':
            print('Code:', self._III_year__reg_no[2:5])
            self.department = 'BCA'
            print('Department :', self.department)
            self.course = 'Computer Application'
            print('Course Name :', self.course)


class access1(College_I, College_II, College_III):
    def access(self):
        if hasattr(self, '_II_year__reg_no') and self._II_year__reg_no[0:2] == '22':
            std = College_II()
            std._College_II__department()
        
        elif hasattr(self, '_I_year__reg_no') and self._I_year__reg_no[0:2] == '23':
            std = College_I()
            std._College_I__department()
        
        elif hasattr(self, '_III_year__reg_no') and self._III_year__reg_no[0:2] == '21':
            std = College_III()
            std._College_III__department()
    

authen = access1()
authen.access()
