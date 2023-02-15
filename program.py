class Subject:
    """
    This class stores the credit and grade point of a subject.
    """

    # constructor
    def __init__(self, credit, grade_point):

        # check if the credit and grade point are integers and are not negative
        if type(credit) != int:
            raise TypeError("Credit should be an integer.")
        if type(grade_point) != int:
            raise TypeError("Grade Point should be an integer.")
        if credit < 0 or grade_point < 0:
            raise ValueError("Credit and Grade Point cannot be negative.")
        
        
        self.credit = credit
        self.grade_point = grade_point

    def __str__(self):
        return "Credit: " + str(self.credit) + "\nGrade Point: " + str(self.grade_point)


class Gpa(Subject):
    """
    This class calculates the GPA of a student.
    It takes the credit and grade point of each subject as input and returns the GPA.
    """

    # Class variables
    # maintains no of subjects added
    no_of_subjects = 0

    # Constructor
    def __init__(self):
        self.gpa = 0.0
        self.numerator = 0.0
        self.denominator = 0.0
        self.sub=[]

    # Add a subject
    def addsubject(self, credit, grade_point):
        """
        addsubject(credit, grade_point)
        This function adds a subject to the list of subjects.
        """


        # limits on credit and grade point

        if credit > 8:
            raise ValueError("Credit cannot be greater than 8.")
        if grade_point > 10:
            raise ValueError("Grade Point cannot be greater than 10.")
            
        
        # Add subject to the list
        self.sub.append(Subject(credit, grade_point))
        self.no_of_subjects += 1

    # Calculate GPA
    def calc(self):
        """
        calc()
        This function calculates the GPA of the student.
        """

        if self.no_of_subjects == 0:
            raise ValueError("No subjects added yet. Run addsubject(credit, grade_point) first.")
            
        # Iterate through the list of subjects and calculate the numerator and denominator
        for i in range(self.no_of_subjects):
            self.numerator += self.sub[i].credit * self.sub[i].grade_point
            self.denominator += self.sub[i].credit
        
        # Calculate the GPA with the numerator and denominator
        self.gpa = self.numerator / self.denominator

        # Check if GPA is valid
        if self.gpa > 10:
            print("GPA cannot be greater than 10. Please check your inputs.")
            return

        return self.gpa

    def display(self):
        """
        display()
        This function displays the number of subjects and the GPA.
        """


        # Check if at least one subject is added
        if self.no_of_subjects == 0:
            raise ValueError("No subjects added yet. Run addsubject(credit, grade_point) first.")
            

       

        # Check if GPA is calculated
        if self.gpa == 0.0:
            raise ValueError("No GPA calculated yet. Run calc() first.")
            
        
        # Display the number of subjects and the GPA
        print("No of subjects: ", self.no_of_subjects)
        print("GPA: ", self.gpa)
    
    def __str__(self):

        if self.no_of_subjects == 0:
            return "No subjects added yet. Run addsubject(credit, grade_point) first."
        
        return "No of subjects: " + str(self.no_of_subjects) + "GPA: " + str(self.gpa)
    


def main():
    # Create an object of the gpa class
    gpa1 = gpa()

    # Add subjects
    gpa1.addsubject(2, 8)
    gpa1.addsubject(3, 8)
    gpa1.addsubject(3, 7)
    gpa1.addsubject(4, 8)
    gpa1.addsubject(2, 10)
    gpa1.addsubject(4, 9)
    gpa1.addsubject(4, 9)
    gpa1.addsubject(3, 8)

    # Calculate the GPA
    gpa1.calc()

    # Display the results
    gpa1.display()


if __name__ == "__main__":
    main()