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
        ### CONTAINS OF PROJECT
        1. Rank - Ranking of overall sales
        2. Name - The games name
        3. Platform - Platform of the game release(eg- PC,PS4,etc.)
        4. Year of the game's release
        5. Genre - Genre of the game
        6. Publisher - Publisher of the game
    """)
    st.markdown("""
        ### INTRODUCTION
        A video game is an electronic game that can be played on a computing device, such as a personal
        computer, gaming console or mobile phone. Depending on the platform, video games can be
        subcategorized into computer games and console games. In recent years, however, the emergence of
        social networks, smartphones and tablets introduced new categories such as mobile and social games
        Video games have come a long way since the first games emerged in the 1970s. Today’s video games offer
        photorealistic graphics and simulate reality to a degree which is astonishing in many cases.
    """)
    st.markdown("""
        ### STATISTICS ON THE TOPIC
        1. Global overview
        2. U.S. overview
        3. Market leaders
        4. Hardware market and ownership
        5. Software
        6. consumer behavior
    """)
    st.image('game sales.jpg')


def viewDataset():
    st.header("Dataset Details")


def analyseTimeline():
    st.header("Timeline analysis")
    st.markdown('---')

    col1, col2 = st.beta_columns(2)

    col1.line_chart(analysis.getYearCount())
    col2.bar_chart(analysis.getYearCount())

    col3, col4 = st.beta_columns(2)

    col3.line_chart(analysis.getYearSum())  
    col4.bar_chart(analysis.getYearSum())

    centuries = ['2010 - 2016']

    popGames = {
        centuries[0] : ['PS4', 'PC', '3DS', 'XOne']
    }

    selPlatforms = popGames[centuries[0]]

    # st.dataframe(analysis.filterPlatform(selPlatforms))


# most profitable platform in different centuries


def analysePlatform():
    st.header("Video Games Platform analysis")
    st.markdown('---')

    st.bar_chart(analysis.getPlatformSum())

    # analyse sum and count in line chart



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

