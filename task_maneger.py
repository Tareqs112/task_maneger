message = '''1.Add task
2.Mark task as combleted
3.View the taskes
4.quit'''
taskes = []

#define vunction to add a task
def add_task():
    task = input("Enter the task that you want to add: ")
    task_info = {"task": task, "completed": False}  # المهمة تكون غير مكتملة افتراضيًا
    taskes.append(task_info)
    print("Task was added successfully!")
    print("-"*30)

# دالة لعرض المهام غير المكتملة وتحديد المهمة كـ "مكتملة"
def mark_task():
    incompleted_taskes = [task for task in taskes if task["completed"] == False]
    if incompleted_taskes:
#print incompleted taskes if there any
        print("in combleted taskes are:")
        for i , task in enumerate(incompleted_taskes,1):
            print(f"{i}.{task["task"]}")
        print("-"*30)
        task_number = int(input("Enter the number of task to comleted: "))
        if incompleted_taskes[task_number-1]["completed"] == False:
           incompleted_taskes[task_number-1]["completed"] =True
           print("Task was completed successfuly!")
           print("-"*30)
    else:
            print("Great!.You don't have any incompleted taskes.")
            print("-"*30)
#define function to print the taskes
def view_taskes(taskes):
    if taskes:
        for i,task in enumerate(taskes,1):
            print(f"{i}.{task["task"]}")
    else:
        print("There's no taskes")
            
        
    
    


while True:
    print(message)
    choice = input("enter the number of what you want to do: ")
    if choice == "1":
        add_task()
        print("-"*30)
    elif choice == "2":
        mark_task()
    elif choice == "3":
        view_taskes(taskes)
        print("-"*30)
    elif choice == "4":
        print("quiting the program...")
        break
    else:
        print("Enter viled number between 1,4")
        print("-"*30)