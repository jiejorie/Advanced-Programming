from tkinter import*
from tkinter import ttk

# main function that calls the parent class and executes the mainloop function
def main():
    student_manager = Student_Manager()
    student_manager.mainloop()

class Student_Manager(Tk): # parent class
    def __init__(self):
        # main setup
        super().__init__()
        self.title("Student Manager")
        self.geometry("700x400")
        self.minsize(700,400)

        # reads studentMarks.txt file
        self.file = open("studentMarks.txt", encoding="utf-8")
        self.read = self.file.readlines() 

        # initializes essential lists and dictionaries
        self.rawData = [line.strip() for line in self.read]
        self.studentData = {}
        self.studentNames = []
        self.compareScores = {}
        self.create_studentNames()

        # Setup widgets 
        self.heading = ttk.Label(self, text="Student Manager", font=("Arial", 18, "bold")).pack(padx=20, pady=15)
        self.Upper_Menu = Upper_Menu(self, self.show_all_records, self.show_highest, self.show_lowest)
        self.Upper_Menu.pack()
        self.Bottom_Menu = Bottom_Menu(self, self.studentNames, self.view_record)
        self.Bottom_Menu.pack()
        self.textBox = Text(self, width=55, height=50)
        self.textBox.pack(pady=25)

    # organizes the student info data
    def get_student_info(self, index):
        pickStudent = self.rawData[index]
        splittedData = pickStudent.split(",")
        idNum, name, score1, score2, score3, examMark = splittedData
        scores = score1, score2, score3, examMark
        scoresList = [int(score) for score in scores]
        courseworkSum = sum(scoresList) - scoresList[-1]
        percentage = (sum(scoresList)/160) * 100
        if percentage < 40:
            grade = "F"
        elif percentage >= 70:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        else:
            grade = "D"
        return splittedData, idNum, name, examMark, scores, courseworkSum, percentage, grade

    # creates a list of all the student's names
    def create_studentNames(self):
        amount = self.rawData[0]
        studentAmount = int(amount) 
        for numCounter in range(studentAmount):
            index = numCounter+1
            splittedData, idNum, name, examMark, scores, courseworkSum, percentage, grade = self.get_student_info(index)
            self.studentNames.append(name.strip())

    # compares the scores and retrieves the target value
    def find_student_with_score(self, neededScore):
        for key, value in self.compareScores.items():
            if value == neededScore:
                return key
   
    # displays all the student records
    def show_all_records(self):
        self.textBox.delete("1.0", "end")
        amount = self.rawData[0]
        studentAmount = int(amount) 
        for numCounter in range(studentAmount):
            if numCounter <= studentAmount:
                index = numCounter+1
                splittedData, idNum, name, examMark, scores, courseworkSum, percentage, grade = self.get_student_info(index)
                self.studentData[name] = idNum, courseworkSum, examMark, percentage, grade
                self.textBox.insert(END, f"\n{numCounter+1}.)\nStudent Name: {name}\nStudent idNum: {idNum}\nCoursework Total : {courseworkSum}\nExam Mark: {examMark}\nOverall Percentage: {percentage:.2f}%\nGrade: {grade}\n")
        percentages = [p[3] for p in self.studentData.values()]
        pAverage = sum(percentages) / len(percentages)
        self.textBox.insert(END, f"\nTotal Number of Students: {studentAmount}\nClass pAverage Percentage: {pAverage:.2f}%")

    # displays the info of the student with the highest score
    def show_highest(self):
        self.textBox.delete("1.0", "end")
        for student in self.rawData:
            if student != self.rawData[0]:
                index = self.rawData.index(student)
                splittedData, idNum, name, examMark, scores, courseworkSum, percentage, grade = self.get_student_info(index)
                self.studentData[name] = idNum, courseworkSum, examMark, percentage, grade
                self.compareScores[name]= percentage
            if student == self.rawData[-1]:
                neededScore = max(self.compareScores.values())
                studentFound = self.find_student_with_score(neededScore)
                if (studentFound, neededScore) in self.compareScores.items():
                    infoValues = self.studentData.get(studentFound)
                    self.textBox.insert(END, f"\nStudent Name: {studentFound}\nStudent idNum: {infoValues[0]}\nCoursework Total : {infoValues[1]}\nExam Mark: {infoValues[2]}\nOverall Percentage: {infoValues[3]:.2f}%\nGrade: {infoValues[4]}\n")
    
    # displays the info of the student with the lowest score
    def show_lowest(self):
        self.textBox.delete("1.0", "end")
        for student in self.rawData:
            if student != self.rawData[0]:
                index = self.rawData.index(student)
                splittedData, idNum, name, examMark, scores, courseworkSum, percentage, grade = self.get_student_info(index)
                self.studentData[name] = idNum, courseworkSum, examMark, percentage, grade
                self.compareScores[name]= percentage
            if student == self.rawData[-1]:
                neededScore = min(self.compareScores.values())
                studentFound = self.find_student_with_score(neededScore)
                if (studentFound, neededScore) in self.compareScores.items():
                    infoValues = self.studentData.get(studentFound)
                    self.textBox.insert(END, f"\nStudent Name: {studentFound}\nStudent idNum: {infoValues[0]}\nCoursework Total : {infoValues[1]}\nExam Mark: {infoValues[2]}\nOverall Percentage: {infoValues[3]:.2f}%\nGrade: {infoValues[4]}\n")

    # displays the info of any chosen student
    def view_record(self):
        self.textBox.delete("1.0", "end")
        for student in self.rawData:
            if student != self.rawData[0]:
                index = self.rawData.index(student)
                splittedData, idNum, name, examMark, scores, courseworkSum, percentage, grade = self.get_student_info(index)
                self.studentData[name.strip()] = idNum, courseworkSum, examMark, percentage, grade
            if student == self.rawData[-1]:
                studentFound = self.Bottom_Menu.studentList.get().title()
                if studentFound in self.studentData:
                    infoValues = self.studentData.get(studentFound)
                    self.textBox.insert(END, f"\nStudent Name: {studentFound}\nStudent idNum: {infoValues[0]}\nCoursework Total : {infoValues[1]}\nExam Mark: {infoValues[2]}\nOverall Percentage: {infoValues[3]:.2f}%\nGrade: {infoValues[4]}\n")

# frame for the upper menu of buttons
class Upper_Menu(ttk.Frame):
    def __init__(self, parent, show_all_records, show_highest, show_lowest):
        super().__init__(parent)
        self.allRecordsbtn = ttk.Button(self, text="View all student records", command=show_all_records).grid( ipadx= 10, ipady= 5, padx=10, pady=20, row=0, column=0)
        self.highestScorebtn = ttk.Button(self, text="Show Highest Score", command=show_highest).grid(ipadx=10, ipady=5, padx=10, pady=20, row=0, column=1)
        self.lowestScorebtn = ttk.Button(self, text="Show Lowest Score", command=show_lowest).grid(ipadx=5, ipady=5, padx=10, pady=20, row=0, column=2)

# frame for the bottom menu of widgets
class Bottom_Menu(ttk.Frame):
    def __init__(self, parent, studentNames, view_record):
        super().__init__(parent)
        self.studentNames = studentNames
        self.textlbl = ttk.Label(self, text="View Individual Student Records:", font=("Arial", 9, "bold")).grid(padx=5, row=0, column=0 )
        self.studentList = ttk.Combobox(self, value=studentNames)
        self.studentList.current(0)
        self.studentList.grid(padx=5, row=0, column=1)
        self.viewRecordbtn = ttk.Button(self, text="View Record", command=view_record).grid(ipadx=5, ipady=5, row=0, column=2)

# if the current script is directly running, the code will run
if __name__ == "__main__":
    main()
