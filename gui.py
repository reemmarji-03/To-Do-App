import functions 
import FreeSimpleGUI as g
import time

g.theme("Purple")

label = g.Text("Type in a to-do")
label_clock = g.Text('', key='clock')
input_box = g.InputText(tooltip="Enter to-do", key="todo")
add_button = g.Button("Add", size=[10, 1])
list_box = g.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=[45,10])
edit_button = g.Button("Edit")

complete_button = g.Button("Complete")
exit_button = g.Button("Exit")

window = g.Window("My To-Do App", 
                 layout=[[label_clock],
                         [label],
                         [input_box, add_button], 
                         [list_box, edit_button, complete_button],
                         [exit_button]], 
                 font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            todo = values['todo']+'\n'
            todos.append(todo.capitalize())
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'Edit':
            try:
                todos = functions.get_todos()
                print(todos)
                todo_to_edit = values['todos'][0]

                print(todo_to_edit)
                new_todo = values['todo']+'\n'

                index = todos.index(todo_to_edit)
        
                todos[index]=new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                g.popup("Select an item first!")
        
        case 'Complete':
            try:
                todos = functions.get_todos()
                todo_to_remove = values['todos'][0]
                todos.remove(todo_to_remove)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                g.popup("Select an item first!")

        case 'Exit':
            break
        
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case g.WIN_CLOSED:
            break

window.close()
