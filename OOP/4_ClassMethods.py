class Student:
    
    num_of_stds = 0    #defining a class variable which is applicable to the whole class
    
    def __init__(self, first, last, roll, bloodType): #Initialise self 
        self.first = first
        self.last = last
        self.roll = roll
        self.bloodType = bloodType
        self.email = first + '.' + last + '@school.nz'

        
            
        
        Student.num_of_stds += 1  #Adding 1 to class variable of number of students
                                  #everytime a new entry is added

    def Bt(self):                 #returning a bloodType function   
        return'{} bloodtype is {}'.format(self.first, self.bloodType)
    
@classmethod
def randomClassMethod(cls):
    pass


student1 = Student('Tom', 'Cruise', '001', 'A+')
student2 = Student('James', 'Bond', '007','B-')
student3 = Student('Harry', 'Mcloughlin', '003','AB-')


print(student1.first)
print(Student.num_of_stds)
print(student3.email)
print(student2.Bt())

