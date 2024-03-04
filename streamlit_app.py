
import streamlit as st


st.title('我的第一个Streamlit应用')
st.write('欢迎来到Streamlit的世界！')

name = st.text_input('请输入你的名字')
age = st.slider('请选择你的年龄', 0, 100, 25)

st.write(f'你好，{name}！你的年龄是{age}岁。')