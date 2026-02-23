import streamlit as st
import  functions


todos = functions.get_todos()

st.title("Todos")
st.subheader("This is my todo app")
st.write("Tis app is to increase your productivity.")

for index, todo in enumerate(todos):
    label = todo.strip()
    if st.checkbox(label, key=f"todo_{index}"):
        todos.pop(index)
        functions.write_todos(todos)
        st.rerun()

def add_todo_new():
    new_todo = st.session_state["new_todo"].strip()
    if not new_todo:
        return
    todos.append(new_todo + "\n")
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""

st.text_input(label="",placeholder="Enter todo",
                       on_change=add_todo_new,key='new_todo')

#st.session_state
#hfh