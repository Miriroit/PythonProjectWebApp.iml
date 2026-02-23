import streamlit as st
import  functions


todos = functions.get_todos()

st.title("Todos")
st.subheader("This is my todo app")
st.write("Tis app is to increase your productivity.")

for index,todo in enumerate(todos):
   checkbox= st.checkbox(todo,key=todo)
   if checkbox:
       todos.pop(index)
       functions.write_todos(todos)
       del st.session_state[todo]
       st.rerun()

def add_todo_new():
    st.session_state["new_todo"]
    todos.append(todo +"\n")
    functions.write_todos(todos)


st.text_input(label="",placeholder="Enter todo",
                       on_change=add_todo_new,key='new_todo')

#st.session_state