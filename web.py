import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("MY To-do App")
st.subheader("This is your To-do app")
st.write("This app is to increase your productivity")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=index)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index]
        st.experimental_rerun()
st.text_input(label="", placeholder="Add a new to do",
              on_change=add_todo,
              key="new_todo")