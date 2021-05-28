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
