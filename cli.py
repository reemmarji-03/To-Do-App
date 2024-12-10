from functions import get_todos, write_todos  
import time 
from datetime import datetime
import lookups

print(time.strftime("%b %d, %Y -- %H:%M"))

while True:
    action=input(lookups.first_input_statement)
    action = action.strip()
    if action.startswith('add'):
            todo = action[4:]
            todos = get_todos()
            todos.append(todo.capitalize()+'\n')
            write_todos(todos)

    elif action.startswith('show'):

            todos = get_todos()

            for index, i in enumerate(todos):
                i = i.strip('\n')
                row = f"{index + 1}- {i}"
                print(row)

    elif action.startswith('edit'):
        try:
            c = int(action[5:])
            new = input("Edit: ")

            todos = get_todos()
            todos[c-1] = new + '\n'
            write_todos(todos)

        except ValueError:
             print(lookups.invalid_command_statement)
             continue
             
    elif action.startswith('complete'):
        try:
            remove = int(input("Item number to complete: "))

            todos = get_todos()
            todo_to_remove = todos[remove-1].strip('\n')
            todos.pop(remove-1)
            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list!"
            print(message)
        except IndexError:
             print(lookups.not_found_statement)
             continue

    elif action.startswith('exit'):
            break
    else:
        print(lookups.invalid_command_statement)

print(lookups.final_statement)