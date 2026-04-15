exam=int(input("How many exam grades dose each student have?"))
while True:

    print("Enter the exam grades")

    total = 0
    for i in range(1, exam + 1):
        grades = float(input(f"Exam {i}: "))
        total += grades
    average = total / exam
    print("The average is ",average)
    anotherStudent=input("Enter exam grades for another student(Y/N)?")
    if anotherStudent !='y':
        break
        
       
        
    