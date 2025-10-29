from tkinter import*
from tkinter import ttk

root = Tk()
root.title("Student Manager")
root.geometry("700x400")

file = open("studentMarks.txt", encoding="utf-8")
read = file.readlines()

rawData = [line.strip() for line in read]
studentData = {}
studentNames = []
compareScores = {}

def get_student_info(index):
    pickStudent = rawData[index]
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

def create_studentNames():
    amount = rawData[0]
    studentAmount = int(amount) 
    for numCounter in range(studentAmount):
        index = numCounter+1
        splittedData, idNum, name, examMark, scores, courseworkSum, percentage, grade = get_student_info(index)
        studentNames.append(name.strip())

listStudentNames = create_studentNames()
        
def find_student_with_score(neededScore):
    for key, value in compareScores.items():
        if value == neededScore:
            return key

def show_all_records():
    textBox.delete("1.0", "end")
    amount = rawData[0]
    studentAmount = int(amount) 
    for numCounter in range(studentAmount):
        if numCounter <= studentAmount:
            index = numCounter+1
            splittedData, idNum, name, examMark, scores, courseworkSum, percentage, grade = get_student_info(index)
            studentData[name] = idNum, courseworkSum, examMark, percentage, grade
            textBox.insert(END, f"\n{numCounter+1}.)\nStudent Name: {name}\nStudent idNum: {idNum}\nCoursework Total : {courseworkSum}\nExam Mark: {examMark}\nOverall Percentage: {percentage:.2f}%\nGrade: {grade}\n")
    percentages = [p[3] for p in studentData.values()]
    pAverage = sum(percentages) / len(percentages)
    textBox.insert(END, f"\nTotal Number of Students: {studentAmount}\nClass pAverage Percentage: {pAverage:.2f}%")

def show_highest():
    textBox.delete("1.0", "end")
    for student in rawData:
        if student != rawData[0]:
            index = rawData.index(student)
            splittedData, idNum, name, examMark, scores, courseworkSum, percentage, grade = get_student_info(index)
            studentData[name] = idNum, courseworkSum, examMark, percentage, grade
            compareScores[name]= percentage
        if student == rawData[-1]:
            neededScore = max(compareScores.values())
            studentFound = find_student_with_score(neededScore)
            if (studentFound, neededScore) in compareScores.items():
                infoValues = studentData.get(studentFound)
                textBox.insert(END, f"\nStudent Name: {studentFound}\nStudent idNum: {infoValues[0]}\nCoursework Total : {infoValues[1]}\nExam Mark: {infoValues[2]}\nOverall Percentage: {infoValues[3]:.2f}%\nGrade: {infoValues[4]}\n")

def show_lowest():
    textBox.delete("1.0", "end")
    for student in rawData:
        if student != rawData[0]:
            index = rawData.index(student)
            splittedData, idNum, name, examMark, scores, courseworkSum, percentage, grade = get_student_info(index)
            studentData[name] = idNum, courseworkSum, examMark, percentage, grade
            compareScores[name]= percentage
        if student == rawData[-1]:
            neededScore = min(compareScores.values())
            studentFound = find_student_with_score(neededScore)
            if (studentFound, neededScore) in compareScores.items():
                infoValues = studentData.get(studentFound)
                textBox.insert(END, f"\nStudent Name: {studentFound}\nStudent idNum: {infoValues[0]}\nCoursework Total : {infoValues[1]}\nExam Mark: {infoValues[2]}\nOverall Percentage: {infoValues[3]:.2f}%\nGrade: {infoValues[4]}\n")

def view_record():
    textBox.delete("1.0", "end")
    for student in rawData:
        if student != rawData[0]:
            index = rawData.index(student)
            splittedData, idNum, name, examMark, scores, courseworkSum, percentage, grade = get_student_info(index)
            studentData[name.strip()] = idNum, courseworkSum, examMark, percentage, grade
        if student == rawData[-1]:
            studentFound = studentList.get().title()
            if studentFound in studentData:
                infoValues = studentData.get(studentFound)
                textBox.insert(END, f"\nStudent Name: {studentFound}\nStudent idNum: {infoValues[0]}\nCoursework Total : {infoValues[1]}\nExam Mark: {infoValues[2]}\nOverall Percentage: {infoValues[3]:.2f}%\nGrade: {infoValues[4]}\n")

heading = ttk.Label(root, text="Student Manager", font=("Arial", 18, "bold")).pack(padx=20, pady=15)

MenuFrame1 = ttk.Frame(root)
MenuFrame2 = ttk.Frame(root)

MenuFrame1.pack()
MenuFrame2.pack()

allRecordsbtn = ttk.Button(MenuFrame1, text="View all student records", command=show_all_records).grid( ipadx= 10, ipady= 5, padx=10, pady=20, row=0, column=0)
highestScorebtn = ttk.Button(MenuFrame1, text="Show Highest Score", command=show_highest).grid(ipadx=10, ipady=5, padx=10, pady=20, row=0, column=1)
lowestScorebtn = ttk.Button(MenuFrame1, text="Show Lowest Score", command=show_lowest).grid(ipadx=5, ipady=5, padx=10, pady=20, row=0, column=2)


textlbl = ttk.Label(MenuFrame2, text="View IndividNumual Student Records:", font=("Arial", 9, "bold")).grid(padx=5, row=0, column=0 )
studentList = ttk.Combobox(MenuFrame2, value=studentNames)
studentList.current(0)
studentList.grid(padx=5, row=0, column=1)
viewRecordbtn = ttk.Button(MenuFrame2, text="View Record", command=view_record).grid(ipadx=5, ipady=5, row=0, column=2)

textBox = Text(root, width=55, height=50)
textBox.pack(pady=25)
root.mainloop()
