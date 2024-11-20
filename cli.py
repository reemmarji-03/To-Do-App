from functions import get_todos, write_todos  
import time 
from datetime import datetime

print(time.strftime("%b %d, %Y -- %H:%M"))

while True:
    action=input("Select show, add, edit, complete, or exit: ")
    action = action.strip()
    if action.startswith('add'):
            todo = action[4:]
            todos = get_todos('todos.txt')
            todos.append(todo.capitalize()+'\n')
            write_todos('todos.txt', todos)

    elif action.startswith('show'):

            todos = get_todos('todos.txt')

            for index, i in enumerate(todos):
                i = i.strip('\n')
                row = f"{index + 1}- {i}"
                print(row)

    elif action.startswith('edit'):
        try:
            c = int(action[5:])
            new = input("Edit: ")

            todos = get_todos('todos.txt')
            todos[c-1] = new + '\n'
            write_todos('todos.txt', todos)

        except ValueError:
             print("Your command is invalid")
             continue
             
    elif action.startswith('complete'):
        try:
            remove = int(input("Item number to complete: "))

            todos = get_todos('todos.txt')
            todo_to_remove = todos[remove-1].strip('\n')
            todos.pop(remove-1)
            write_todos('todos.txt', todos)

            message = f"Todo {todo_to_remove} was removed from the list!"
            print(message)
        except IndexError:
             print("Item is not in the list")
             continue

    elif action.startswith('exit'):
            break
    else:
        print("Invalid Command")

print("all done!!")