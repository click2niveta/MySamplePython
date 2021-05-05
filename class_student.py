class Student:
    grades=[]

    def __init__(self,name,id):
        self.name=name
        self.id=id
    def __str__(self):
        return "Name : "+self.name+'\n'+\
               "Id : "+self.id+'\n'+\
               "Grades : "+self.showGrades()
    def addGrades(self,grade):
        self.grades.append(grade)
    def showGrades(self):
        grds=''
        for grade in self.grades:
            grds+=str(grade)+' '
        return grds
    def average(self):
        total=0
        for grade in self.grades:
            total=total+grade
        return total/len(self.grades)

st1=Student("Jane","1075096")
st1.addGrades(90)
st1.addGrades(98)
st1.addGrades(79)
st1.addGrades(81)
st1.addGrades(87)
print(st1)
print("Grades: "+st1.showGrades())
print("Average of Grades: "+str(st1.average()))
