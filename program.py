
class subject:

    def __init__(self, credit, grade_point):
        self.credit = credit
        self.grade_point = grade_point

    def __str__(self):
        return "Credit: " + str(self.credit) + "\nGrade Point: " + str(self.grade_point)

class gpa(subject):
    no_of_subjects = 0

    def __init__(self):
        self.gpa = 0.0
        self.numerator = 0.0
        self.denominator = 0.0
        self.sub=[]

    def addsubject(self, credit, grade_point):
        self.sub.append(subject(credit, grade_point))
        self.no_of_subjects += 1

        
    def calc(self):
        for i in range(self.no_of_subjects):
            self.numerator += self.sub[i].credit * self.sub[i].grade_point
            self.denominator += self.sub[i].credit
        self.gpa = self.numerator / self.denominator
        return self.gpa

    def display(self):
        print("No of subjects: ", self.no_of_subjects)
        print("GPA: ", self.gpa)
    
    def __str__(self):
        return "No of subjects: " + str(self.no_of_subjects) + "GPA: " + str(self.gpa)
    
def main():
    gpa1 = gpa()
    gpa1.addsubject(2, 8)
    gpa1.addsubject(3, 8)
    gpa1.addsubject(3, 7)
    gpa1.addsubject(4, 8)
    gpa1.addsubject(2, 10)
    gpa1.addsubject(4, 9)
    gpa1.addsubject(4, 9)
    gpa1.addsubject(3, 8)

    gpa1.calc()
    gpa1.display()

if __name__ == "__main__":
    main()