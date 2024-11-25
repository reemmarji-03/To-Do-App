import streamlit as st 
import functions


st.title("My Todo App")
st.subheader("Welcome to your to-do list")


todos = functions.get_todos()
for todo in todos:
    st.checkbox(todo)

st.text_input(label= "Enter a todo:", placeholder="Add a todo")



