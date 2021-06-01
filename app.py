import streamlit as st


st.title("Video Game Sales Analysis")
st.image('title_image.jpg')
st.header("A Not very long description")

sidebar = st.sidebar
sidebar.header("Choose Your Option")
choices = ["Select any option below", "View Dataset", "Analyse Timeline"]
selOpt = sidebar.selectbox("Choose what to do", choices)

def projectOverview():
    st.header('Project Overview')
    

def viewDataset():
    st.header("Dataset Details")
    

def analyseTimeline():
    st.header("Timeline analysis")


if selOpt == choices[0]:
    projectOverview()
elif selOpt == choices[1]:
    viewDataset()
elif selOpt == choices[2]:
    analyseTimeline()

def intro():

    st.markdown(""" 
        ### Contains of Project
        1. Rank - Ranking of overall sales
        2. Name - The games name
        3. Platform - Platform of the game release(eg- PC,PS4,etc.)
        4. Year of the game's release
        5. Genre - Genre of the game
        6. Publisher - Publisher of the game
    """)