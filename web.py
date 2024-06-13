import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity. Type in your todos in the input to create your todo list. Click on any todo to mark it as done")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add todo...",
              on_change=add_todo, key="new todo")
