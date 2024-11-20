import functions 
import cli
import FreeSimpleGUI as g

label = g.Text("Type in a to-do")
input_box = g.InputText(tooltip="Enter to-do")
add_button = g.Button("Add")

window = g.Window("My To-Do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()
