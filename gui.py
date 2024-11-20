import functions 
import FreeSimpleGUI as g

label = g.Text("Type in a to-do")
input_box = g.InputText(tooltip="Enter to-do", key="todo")
add_button = g.Button("Add")

window = g.Window("My To-Do App", 
                 layout=[[label], [input_box, add_button]], 
                 font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case 'Add':
            todos = functions.get_todos()
            todo = values['todo']
            todos.append(todo.capitalize()+'\n')
            functions.write_todos(todos)
        case g.WIN_CLOSED:
            break

window.close()
