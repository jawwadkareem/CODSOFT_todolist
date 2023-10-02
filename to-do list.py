import sys


class ToDoList:
    tasks = []
    completed_tasks = []
    def __init__(self):
        print()
        print('Welcome to ToDoList Application')
        print('1. Add Task\n2. Views Tasks\n3. Update Task\n4. Exit')
        choice = int(input('Your Choice: '))
        print()
        if choice == 1:
            self.add_task()
            self.__init__()

        elif choice == 2:
            print(self)
            self.__init__()
        elif choice == 3:
            self.update_task()
            self.__init__()

        if choice == 4:
            sys.exit()

    def __str__(self):
        x = ''
        if len(self.tasks)==0:
            x+= 'No tasks available'

        else:
            for i in range(len(self.tasks)):
                x+=f'{i+1}. {self.tasks[i]}\n'

        if len(self.completed_tasks) == 0:
            x += '\nNo completed tasks\n'
        else:
            x += '\nCompleted Tasks\n'
            for i in range(len(self.completed_tasks)):
                x += f'{i + 1}. {self.completed_tasks[i]}\n'
        return x
    def add_task(self):
        task = input('Enter task: ')
        self.tasks.append(task)
        print('Task Added Successfully')


    def update_task(self):
        print(self)
        markdone = int(input("Enter task number: "))
        taskcomp = self.tasks.pop(markdone-1)
        self.completed_tasks.append(taskcomp)
mylist = ToDoList()