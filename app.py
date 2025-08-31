import streamlit as st

st.set_page_config(page_title="Preksha's To-Do List", page_icon="📝", layout="centered")

st.title("📝 Preksha's To-Do List App")
st.write("A simple app to manage your daily tasks.")


if "tasks" not in st.session_state:
    st.session_state.tasks = []


new_task = st.text_input("Add a new task:")
if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append({"task": new_task, "done": False})


st.subheader("Your Tasks")
for i, t in enumerate(st.session_state.tasks):
    c1, c2 = st.columns([6,1])
    with c1:
        if t["done"]:
            st.markdown(f"✅ ~{t['task']}~")
        else:
            st.markdown(f"🔹 {t['task']}")
    with c2:
        if st.button("✔️", key=i):
            st.session_state.tasks[i]["done"] = True
