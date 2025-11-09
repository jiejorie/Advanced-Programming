from tkinter import*
from tkinter import messagebox
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

        # reads studentMarks.txt file
        self.file = open("studentMarks.txt", encoding="utf-8")
        self.read = self.file.readlines() 

        # initializes essential lists and dictionaries
        self.rawData = [line.strip() for line in self.read]
        self.studentData = {}
        self.studentNames = []
        self.compareScores = {}
        self.create_studentNames()
        self.decoLine = "-------------------------------------------------------------"

        self.columnconfigure(0, weight=1)
        self.rowconfigure((0,1,2), weight=1)
        self.rowconfigure(3, weight=3)
        
        # Setup widgets 
        self.heading = ttk.Label(self, text="Student Manager", font=("Segoe UI Bold", 18)).pack(padx=20, pady=25)
        self.Upper_Menu = Upper_Menu(self, self.show_all_records, self.show_highest, self.show_lowest)
        self.Upper_Menu.pack()
        self.Bottom_Menu = Bottom_Menu(self, self.studentNames, self.view_record)
        self.Bottom_Menu.pack()
        self.textBox = Text(self, height= 7, font=("Segoe UI Semibold", 11), padx=15)
        self.textBox.pack(pady=20, padx=130, anchor="center", expand=True, fill="both")

        # exit popup
        self.protocol("WM_DELETE_WINDOW", self.before_close)

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
                self.textBox.insert(END, f"\n{numCounter+1} {self.decoLine}\n\nStudent Name: {name}\nStudent ID: {idNum}\nCoursework Total : {courseworkSum} pts.\nExam Mark: {examMark} pts.\nOverall Percentage: {percentage:.2f}%\nGrade: {grade}\n")
        percentages = [p[3] for p in self.studentData.values()]
        pAverage = sum(percentages) / len(percentages)
        self.textBox.insert(END, f"\n{self.decoLine}\n{self.decoLine}\n\nTotal Number of Students: {studentAmount}\nClass Average Percentage: {pAverage:.2f}%\n")

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
                    self.textBox.insert(END, f"\nStudent Name: {studentFound}\nStudent ID: {infoValues[0]}\nCoursework Total : {infoValues[1]} pts.\nExam Mark: {infoValues[2]} pts.\nOverall Percentage: {infoValues[3]:.2f}%\nGrade: {infoValues[4]}\n")
    
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
                    self.textBox.insert(END, f"\nStudent Name: {studentFound}\nStudent ID: {infoValues[0]}\nCoursework Total : {infoValues[1]} pts.\nExam Mark: {infoValues[2]} pts.\nOverall Percentage: {infoValues[3]:.2f}%\nGrade: {infoValues[4]}\n")

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
                    self.textBox.insert(END, f"\nStudent Name: {studentFound}\nStudent ID: {infoValues[0]}\nCoursework Total : {infoValues[1]}\nExam Mark: {infoValues[2]}\nOverall Percentage: {infoValues[3]:.2f}%\nGrade: {infoValues[4]}\n")

    # popup to confirm exit
    def before_close(self):
        if messagebox.askyesno("Exit Student Manager","Do you really want to exit?"):
            self.destroy()
        else:
            pass

# frame for the upper menu of buttons
class Upper_Menu(ttk.Frame):
    def __init__(self, parent, show_all_records, show_highest, show_lowest):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)
        self.allRecordsbtn = ttk.Button(self, text="View all student records", command=show_all_records).grid(ipadx=10, ipady=10, padx= 5, pady=10, row=0, column=0, sticky="ew")
        self.highestScorebtn = ttk.Button(self, text="Show Highest Score", command=show_highest).grid(ipadx=10, ipady=10, padx= 5, pady=10, row=0, column=1, sticky="ew")
        self.lowestScorebtn = ttk.Button(self, text="Show Lowest Score", command=show_lowest).grid(ipadx=10, ipady=10, padx= 5, pady=10, row=0, column=2, sticky="ew")

# frame for the bottom menu of widgets
class Bottom_Menu(ttk.Frame):
    def __init__(self, parent, studentNames, view_record):
        super().__init__(parent)
        self.s = ttk.Style()
        self.s.configure("TCombobox", padding=(10,5,0,5))
        self.columnconfigure(0, weight=1)
        self.studentNames = studentNames
        self.textlbl = ttk.Label(self, text="View Individual Records:", font=("Segoe UI Bold", 10)).grid(padx=10, row=0, column=0, sticky="e")
        self.studentList = ttk.Combobox(self, value=studentNames)
        self.studentList.current(0)
        self.studentList.grid(padx=10, row=0, column=1, sticky="ew")
        self.viewRecordbtn = ttk.Button(self, text="View Record", command=view_record).grid(ipadx=10, ipady=10, padx= 10, row=0, column=2, sticky="w")

# if the current script is directly running, the code will run
if __name__ == "__main__":
    main()
