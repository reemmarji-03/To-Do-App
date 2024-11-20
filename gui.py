import functions 
import FreeSimpleGUI as g

label = g.Text("Type in a to-do")
input_box = g.InputText(tooltip="Enter to-do", key="todo")
add_button = g.Button("Add")
list_box = g.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=[45,10])
edit_button = g.Button("Edit")

window = g.Window("My To-Do App", 
                 layout=[[label], [input_box, add_button], [list_box, edit_button]], 
                 font=('Helvetica', 20))

while True:
    event, values = window.read()
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
            todos = functions.get_todos()
            print(todos)
            todo_to_edit = values['todos'][0]
            print(todo_to_edit)
            new_todo = values['todo']+'\n'

            index = todos.index(todo_to_edit)
            todos[index]=new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case g.WIN_CLOSED:
            break

window.close()
