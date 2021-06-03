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
choices = ["Select any option below", "View Dataset",
           "Analyse Timeline", "Analyse Platform", "Analyse Region"]
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


def analyseRegion():
    st.header("Region wise Sales analysis of Video Games")

    st.bar_chart(analysis.getRegionData("NA_Sales"))
    st.bar_chart(analysis.getRegionData("EU_Sales"))
    st.bar_chart(analysis.getRegionData("Global_Sales"))


if selOpt == choices[0]:
    projectOverview()
elif selOpt == choices[1]:
    viewDataset()
elif selOpt == choices[2]:
    analyseTimeline()
elif selOpt == choices[3]:
    analysePlatform()
elif selOpt == choices[4]:
    analyseRegion()


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
