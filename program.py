# modules
from texttable import Texttable

class Subject:
    """
    This class stores the credit and grade point of a subject.
    """

    # constructor
    def __init__(self, credit: int, grade_point: int) -> None:

        # check if the credit and grade point are integers and are not negative
        if type(credit) != int:
            raise TypeError("Credit should be an integer.")
        if type(grade_point) != int:
            raise TypeError("Grade Point should be an integer.")
        if credit < 0 or grade_point < 0:
            raise ValueError("Credit and Grade Point cannot be negative.")
        
        
        self.credit = credit
        self.grade_point = grade_point

    def __str__(self) -> str:
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
    def __init__(self) -> None:
        self.gpa = 0.0
        self.numerator = 0.0
        self.denominator = 0.0
        self.sub=[]

    # Add a subject
    def addsubject(self, credit: int, grade_point: int) -> None:
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
    def calc(self) -> float:
        """
        calc()
        This function calculates the GPA of the student.
        """

        if self.no_of_subjects == 0:
            raise ValueError("No subjects added yet. Run gpa.addsubject(credit, grade_point) first.")
            
        
        
        # Iterate through the list of subjects and calculate the numerator and denominator
        for i in range(self.no_of_subjects):

            # Check if the grade point is less than 5
            if self.sub[i].grade_point < 5:
                continue

            # Calculate the numerator and denominator
            self.numerator += self.sub[i].credit * self.sub[i].grade_point
            self.denominator += self.sub[i].credit
        
        # Calculate the GPA with the numerator and denominator
        self.gpa = self.numerator / self.denominator

        # Check if GPA is valid
        if self.gpa > 10 and self.gpa < 0:
            print("GPA is not valid. Please check your inputs.")
            return

        return self.gpa

    def display(self) -> None:
        """
        display()
        This function displays the number of subjects and the GPA.
        """


        # Check if at least one subject is added
        if self.no_of_subjects == 0:
            raise ValueError("No subjects added yet. Run gpa.addsubject(credit, grade_point) first.")
            

        # Check if GPA is calculated
        if self.gpa == 0.0:
            raise ValueError("No GPA calculated yet. Run gpa.calc() first.")
            
        
        # Display the number of subjects and the GPA
        print("No of subjects: ", self.no_of_subjects)
        print("GPA: ", self.gpa)

    def added(self) -> None:
        """
        added()
        This function displays the subjects added.
        """
        
        table = Texttable()

        table.header(["No.", "Credits", "Grade Points"])
        table.set_cols_dtype(['i', 'i', 'i'])
        table.set_cols_align(['r', 'r', 'r'])

        for i in range(self.no_of_subjects):
            table.add_row([i+1, self.sub[i].credit, self.sub[i].grade_point])

        table.set_deco(Texttable.HEADER)
        print('Subjects added:')
        print(table.draw())
        
    def removesubject(self, index: int) -> None:
        """
        removesubject(index)
        Index values: 1-n
        This function removes a subject from the list of subjects.
        """
        index = index-1
        # Check if the index is valid
        if index > self.no_of_subjects or index < 0:
            raise ValueError(f"Index out of range. Input Index: {index+1} Index Region: 0 to {self.no_of_subjects}")
            
        
        # Remove the subject from the list
        removed = self.sub.pop(index-1)
        self.no_of_subjects -= 1
        print(f'Subject {index + 1} {removed.credit, removed.grade_point} removed successfully.')

    def __repr__(self) -> str:
        return "GPA Calculator"
    
    def __str__(self) -> str:

        if self.no_of_subjects == 0:
            return "No subjects added yet. Run gpa.addsubject(credit, grade_point) first."
        
        return "No of subjects: " + str(self.no_of_subjects) + "GPA: " + str(self.gpa)
    

class Cgpa(Gpa):
    """
    This class calculates the CGPA of a student.
    It takes the GPA of each semester as input and returns the CGPA.
    """

    # Constructor
    def __init__(self):
        self.cgpa = 0.0
        self.total_numerator = 0.0
        self.total_denominator = 0
        self.semester = []
    

    # Add a semester gpa
    def addsemester(self, gpa: Gpa) -> None:
        """
        addsemester(gpa)
        This function adds a semester gpa to the list of semester gpa.
        """

        # Check if the input is of type Gpa else raise an error
        if not isinstance(gpa, Gpa):
            raise TypeError("Input must be of type Gpa.")

        # Check if the gpa is calculatable else raise an error
        if gpa.no_of_subjects <= 0:
            raise ValueError("No subjects added yet. Run gpa.addsubject(credit, grade_point) first.")
        


        gpa.calc()
        self.semester.append(gpa)
            
        
    # Calculate CGPA
    def calc(self) -> float:
        """
        calc()
        This function calculates the CGPA of the student.
        """

        if len(self.semester) == 0:
            raise ValueError("No semesters added yet. Run cgpa.addsemester(gpa) first.")
        
        # Iterate through the list of semester gpa and calculate the numerator and denominator
        for i in range(len(self.semester)):
            self.total_numerator += self.semester[i].numerator
            self.total_denominator += self.semester[i].denominator

        # Calculate the CGPA with the numerator and denominator
        self.cgpa = self.total_numerator / self.total_denominator

        # Check if CGPA is valid
        if self.cgpa > 10 and self.cgpa < 0:
            print("CGPA is not valid. Please check your inputs.")
            return

        return self.cgpa
    
    # Display CGPA
    def display(self) -> None:
        """
        display()
        This function displays the number of semesters and the CGPA.
        """

        if len(self.semester) == 0:
            raise ValueError("No semesters added yet. Run cgpa.addsemester(gpa) first.")
        if self.cgpa == 0.0:
            raise ValueError("No CGPA calculated yet. Run cgpa.calc() first.")
        
        print("No of semesters: ", len(self.semester))
        print("CGPA: ", self.cgpa)
    
    def added(self) -> None:
        """
        added()
        This function displays the semesters added.
        """
        
        table = Texttable()

        table.header(["No.", "GPA", "\u03A3 GP*C", "\u03A3 Credits"])
        table.set_cols_dtype(['i', 'f', 'i', 'i'])
        table.set_cols_align(['r', 'r', 'r', 'r'])

        for i in range(len(self.semester)):
            table.add_row([i+1, self.semester[i].gpa, self.semester[i].numerator, self.semester[i].denominator])

        table.set_deco(Texttable.HEADER)
        print('Semesters added:')
        print(table.draw())

    def removesemester(self, index: int) -> None:
        """
        removesemester(index)
        Index values: 1-n
        This function removes a semester from the list of semesters.
        """
        index = index-1
        # Check if the index is valid
        if index > len(self.semester) or index < 0:
            raise ValueError(f"Index out of range. Input Index: {index+1} Index Region: 0 to {len(self.semester)}")
            
        
        # Remove the semester from the list
        removed = self.semester.pop(index-1)
        print(f'Semester {index+1} {removed.gpa, removed.numerator, removed.denominator} removed successfully.')

    def __repr__(self) -> str:
        return "CGPA Calculator"

    def __str__(self) -> str:
        return "No of semesters: " + str(len(self.semester)) + "CGPA: " + str(self.cgpa)
        

def main():

    print("GPA Calculator")
    print("--------------\n")
    

    # Create an object of the gpa class
    gpa1 = Gpa()

    # Add subjects
    gpa1.addsubject(2, 8)
    gpa1.addsubject(3, 8)
    gpa1.addsubject(3, 7)
    gpa1.addsubject(4, 8)
    gpa1.addsubject(2, 10)
    gpa1.addsubject(4, 9)
    gpa1.addsubject(4, 9)
    gpa1.addsubject(3, 8)
    
    
    gpa1.added()

    # Remove a subject
    gpa1.removesubject(1)
    gpa1.removesubject(2)

    gpa1.added()


    # create an object of the gpa class
    gpa2 = Gpa()

    # Add subjects
    gpa2.addsubject(2, 9)
    gpa2.addsubject(3, 10)
    gpa2.addsubject(3, 7)
    gpa2.addsubject(4, 9)
    gpa2.addsubject(2, 6)
    gpa2.addsubject(4, 10)
    gpa2.addsubject(4, 9)
    gpa2.addsubject(3, 8)

    

    # Create an object of the cgpa class
    cgpa = Cgpa()
    
    cgpa.addsemester(gpa1)
    cgpa.addsemester(gpa2)
    cgpa.added()

    cgpa.removesemester(1)
    cgpa.added()
    
    cgpa.calc()
    cgpa.display()
    
    gpa1.calc()

    # Display the results
    gpa1.display()


if __name__ == "__main__":
    main()