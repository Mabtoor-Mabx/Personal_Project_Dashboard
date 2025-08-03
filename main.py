# Personal Project Dashboard Using Streamlit

# Required Libraries

import streamlit as st
import plotly.express as px
import pandas as pd

# page Configration

st.set_page_config(page_title="My Personal Portfolio", page_icon="💼", layout="wide")

# Header File


st.markdown("<h1 style='text-align: center;'>Hi! 👋👋👋  My Name Is Mabtoor Ul Shafiq</h1>", unsafe_allow_html=True)

st.subheader("Python Developer ||| Computer Science Teacher ||| ML Enthusiast ||| Backend Developer (FLASK + DJANGO)")
st.write('''
Welcome to my Personal Portfolio Dashboard built with streamlit !!!

Here! You will find all information about my background, skills, Personal projects and Experience        
''')

st.markdown("---")


# Add About/Bio Section


st.markdown("<h2 style='text-align: center;'>📌📌📌 About Me!!! 📌📌📌</h2>", unsafe_allow_html=True)

st.write('''
I am Passionate Python Developer and Computer Science Teacher who works as a computer science teacher for previous 3 years. Moreover I have experience to build application (We based Application) and Backend logics using python programmming languages. I have ability to work with different  libraries and frameworks of python including FLASK and DJANGO. I am also work in SQL as a Database engineer. I use Anvil Works for creating We app for pure python and Using Streamlit too for webapp.
''')

st.image("assets/profile.jpg", width=200, caption="Mabtoor Ul Shafiq")

st.markdown("---")

# Add Skills Section

st.markdown("<h2 style='text-align: center;'>🧰🧰🧰 Skills 🧰🧰🧰</h2>", unsafe_allow_html=True)
skills_data = {
    "Skill": ["Python", "SQL", "FLASK", "Anvil Works", "Streamlit"],
    "Level": [80,70,60,90,97]
}

df_skills = pd.DataFrame(skills_data)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Skill Level (Bar Chart) ")
    bar_fig = px.bar(df_skills, x='Skill', y='Level',
                     labels={'Level': 'Proficiency (%)'},
                     text = "Level")
    st.plotly_chart(bar_fig, use_container_width=True)

with col2:
    st.subheader("Languages / Tools Split (Pie Chart)")
    pie_fig = px.pie(df_skills, names='Skill', values="Level")
    st.plotly_chart(pie_fig, use_container_width=True)

st.markdown("---")



# Project Section


st.markdown("<h2 style='text-align: center;'>💡💡💡 Projects 💡💡💡</h2>", unsafe_allow_html=True)


projects  = [
    {
        "name": "Emily - The AI Virtual Assistant",
        "desc": "Emily is a voice-controlled AI virtual assistant built using Python. It can perform various tasks such as providing real-time weather updates, fetching Nobel Prize information, reading top news headlines, and opening popular websites. Emily uses speech recognition for voice input and text-to-speech technology for audio responses, creating an interactive and hands-free experience"
    },
    {
        "name": "Advanced Todo App using Flask",
        "desc": "The Advanced Todo App using Flask is a full-featured web application built with the Flask framework. It allows users to register, log in, and manage their tasks in a simple yet powerful to-do list system. The app utilizes secure authentication, form validation, task tracking, and database integration to provide a smooth and efficient user experience."
    },
    {
        "name": "Calculator With Saved History Using Python",
        "desc": "The Calculator With Saved History Using Python is a simple command-line application that allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division. One of the key features of this project is the ability to save calculation history to a file (history.txt) and retrieve it later. Users can also clear the history when needed, making it a practical and lightweight tool for everyday calculations."
    }
]

for proj in projects:
    st.subheader(proj['name'])
    st.write(proj['desc'])
    st.markdown("---")



# Experience Section


st.markdown("<h2 style='text-align: center;'>📃📃📃 Experience 📃📃📃</h2>", unsafe_allow_html=True)


exp1, exp2 = st.columns(2)


with exp1:
    st.subheader("Computer Science Teacher - The Legacy School")
    st.write("August 2024 - Present")
    st.markdown('''
    Computer Science Teacher at The Legacy School Faisalabad, Pakistan. Handling Computer Science Subjects for Grade 5,6,7 Teaching Different AI Tools and Techniques.
                ''')
    
with exp2:
    st.subheader("Python Developer - Arfaa Tech")
    st.write("December 2022- December 2023")
    st.markdown('''
Performing Different tasks as a Python Backend Developer using Frameworks called Django and Flask, Use Database too like SQL and MYSQL and Deploy Webapp in Streamlit and Anvil Works''')
    
st.markdown("---")


st.success("🎉🎉🎉Thank You For Visiting My Dashbboard 🎉🎉🎉")

# Footer 

st.markdown("<p style='text-align: center;'>© 2025 Mabtoor Ul Shafiq!!! All Rights Reserved </p>", unsafe_allow_html=True)


