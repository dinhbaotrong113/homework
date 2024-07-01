import streamlit as st

st.title("MY PROJECT")
st.header("This is a header")
st.subheader("this is a subheader")
st.text("I love AI Viet Nam")
st.markdown("[AI Viet Nam](https://aivietnam.edu.vn/)")
st.markdown("""
            1. Machine Learning
            2. Deep Learning
            """)
st.markdown("$\sqrt{2x+2}$")
st.latex("\sqrt{2x+2}")
def get_user_name():
    return "Thai"
with st.echo():
    st.write("this code will be printed")
    def get_email():
        return "tedfsdf"
    user_name = get_user_name()
    email = get_email()
    st.write(user_name, email)
    
st.video("D:/Homework/Module1/Week3/source/video.mp4")
st.divider()

agree = st.checkbox("I agree", on_change= get_user_name)
if agree:
    st.write("thank!")

status = st.radio('your Favorite color:', ['yellow', 'blue'], captions = ['vang', 'xanh'])
print(status)

status = st.selectbox('your contact', ['email', 'adress'])
print(status)

st.multiselect('colors:', ['green', 'yellow', 'Blue'], ['yellow'])

slider = st.select_slider('your color:', [0,1,2])
print(slider)
button = st.button('in ket qua')
if button:
    st.write("chao mung ban den binh nguyen vo tan")
else:
    st.write("tam biet")

name = st.text_input('Your Name', value = "thai")
st.write(f'chao mmung {name}')

upload = st.file_uploader('choose files', accept_multiple_files=True)
for ul in upload:
    read_f = ul.read()
    st.write("File Name:", ul.name)


with st.form("my form"):
    col1, col2 = st.columns(2)
    f_name = col1.text_input("name")
    f_age = col2.text_input("Age:")

    submited = st.form_submit_button('submit')
    if submited:
        st.write(f"Name: {f_name}, Age: {f_age}")

import random
value = random.randint(1,10)
if 'key' not in st.session_state:
    st.session_state['email'] = value
    st.session_state['password'] = value
st.write(st.session_state.key)
