import streamlit as st
from analysedata import Analyse


def loadData():
    print('loading..')
    return Analyse('datasets/vgsales.csv')

analysis = loadData()

st.title("Video Game Sales Analysis")
st.image('title_image.jpg')

sidebar = st.sidebar
sidebar.header("Choose Your Option")
choices = ["Select any option below", "View Dataset", "Analyse Timeline", "Analyse Platform"]
selOpt = sidebar.selectbox("Choose what to do", choices)

def projectOverview():
    st.header('Project Overview')
    st.header("A Not very long description")

def viewDataset():
    st.header("Dataset Details")
    

def analyseTimeline():
    st.header("Timeline analysis")
    st.markdown('---')

    col1, col2 = st.beta_columns(2)

    col1.line_chart(analysis.getYearCount())
    col2.bar_chart(analysis.getYearCount())


def analysePlatform():
    st.header("Video Games Platform analysis")
    st.markdown('---')

    st.bar_chart(analysis.getPlatformSum())


if selOpt == choices[0]:
    projectOverview()
elif selOpt == choices[1]:
    viewDataset()
elif selOpt == choices[2]:
    analyseTimeline()
elif selOpt == choices[3]:
    analysePlatform()
