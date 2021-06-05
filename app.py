import streamlit as st
from analysedata import Analyse
import plotly.graph_objects as go


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
    st.markdown(""" 
        ### Contains of Project
        1. Rank - Ranking of overall sales
        2. Name - The games name
        3. Platform - Platform of the game release(eg- PC,PS4,etc.)
        4. Year of the game's release
        5. Genre - Genre of the game
        6. Publisher - Publisher of the game
    """)


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
    n = st.select_slider(
        options=[i*5 for i in range(1, 11)], label="Select No. of Games")
    selRegion = st.selectbox(options=[
        'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales', ], label="Select Region")
    st.bar_chart(analysis.getRegionAndPlatformSum(selRegion, n))

    st.bar_chart(analysis.getRegionAndPlatformCount(selRegion, n))

    st.bar_chart(analysis.getRegionAndPublisherSum(selRegion, n))

    st.bar_chart(analysis.getRegionAndPublisherCount(selRegion, n))

    data = analysis.getRegionSum()
    fig = plotpie(data.index, data.values, 'Total Region Sales')
    st.plotly_chart(fig)


def plotpie(labels, values, title):
    layout = go.Layout(title=title)
    fig = go.Figure(layout=layout)

    fig.add_trace(go.Pie(labels=labels, values=values, textinfo='label+percent', hole=0.2,
                         marker=dict(colors=['#f7d468', '#74cb35'],
                                     line_color='Gray',
                                     line_width=1),
                         textfont={'color': '#000', 'size': 12},
                         textfont_size=12))
    return fig


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
