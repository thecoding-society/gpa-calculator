
class subject:
    """
    This class stores the credit and grade point of a subject.
    """

    def __init__(self, credit, grade_point):
        self.credit = credit
        self.grade_point = grade_point

    def __str__(self):
        return "Credit: " + str(self.credit) + "\nGrade Point: " + str(self.grade_point)


class gpa(subject):
    """
    This class calculates the GPA of a student.
    It takes the credit and grade point of each subject as input and returns the GPA.
    """

    no_of_subjects = 0

    def __init__(self):
        self.gpa = 0.0
        self.numerator = 0.0
        self.denominator = 0.0
        self.sub=[]

    def addsubject(self, credit, grade_point):
        """
        addsubject(credit, grade_point)
        This function adds a subject to the list of subjects.
        """

        if credit < 0 or grade_point < 0:
            print("Credit and Grade Point cannot be negative.")
            return
        if credit > 8:
            print("Credit cannot be greater than 8.")
            return
        if grade_point > 10:
            print("Grade Point cannot be greater than 10.")
            return
        
        self.sub.append(subject(credit, grade_point))
        self.no_of_subjects += 1

        
    def calc(self):
        """
        calc()
        This function calculates the GPA of the student.
        """

        if self.no_of_subjects == 0:
            print("No subjects added yet. Run addsubject(credit, grade_point) first.")
            return

        for i in range(self.no_of_subjects):
            self.numerator += self.sub[i].credit * self.sub[i].grade_point
            self.denominator += self.sub[i].credit
        self.gpa = self.numerator / self.denominator

        if self.gpa > 10:
            print("GPA cannot be greater than 10. Please check your inputs.")
            return

        return self.gpa

    def display(self):
        """
        display()
        This function displays the number of subjects and the GPA.
        """

        if self.no_of_subjects == 0:
            print("No subjects added yet. Run addsubject(credit, grade_point) first and then run calc().")
            return
        if self.gpa == 0.0:
            print("No GPA calculated yet. Run calc() first.")
            return
        
        print("No of subjects: ", self.no_of_subjects)
        print("GPA: ", self.gpa)
    
    def __str__(self):

        if self.no_of_subjects == 0:
            return "No subjects added yet. Run addsubject(credit, grade_point) first."
        
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