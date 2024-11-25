import streamlit as st 
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo+"\n")
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("Welcome to your to-do list")


for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun
    

st.text_input(label= "Enter a todo:", placeholder="Add a todo...",
              on_change=add_todo, key="new_todo")



