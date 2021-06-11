import streamlit as st
from analysedata import Analyse
from visualization import *


def loadData():
    print('loading..')
    return Analyse('datasets/vgsales.csv')


analysis = loadData()

st.title("Video Game Sales Analysis")
st.image('title_image.jpg')

sidebar = st.sidebar
sidebar.header("Choose Your Option")
choices = ["Select any option below", "View Dataset",
           "Analyse Timeline", "Analyse Platform", "Analyse Region", "Analyse Genre"]
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

    df = analysis.getDataframe()

    with st.spinner("Loading Data..."):
        st.markdown(
            '<p class="head"> DataSet Used In This Project</p>', unsafe_allow_html=True)

        st.markdown("")
        st.dataframe(df)

        st.markdown(""" 
        <style>
            .block{
                font-family: Book Antiqua; 
                font-size:24px;
                 padding-top:11%;
                font-weight:light;
                color:lightblue;
            }
        </style>
        """, unsafe_allow_html=True)

        st.markdown('---')
        cols = st.beta_columns(4)
        cols[0].markdown(
            '<p class="block"> Number of Rows : <br> </p>', unsafe_allow_html=True)
        cols[1].markdown(f"# {df.shape[0]}")
        cols[2].markdown(
            '<p class= "block"> Number of Columns : <br></p>', unsafe_allow_html=True)
        cols[3].markdown(f"# {df.shape[1]}")
        st.markdown('---')

        st.markdown('<p class= "head"> Summary </p>', unsafe_allow_html=True)
        st.markdown("")
        st.dataframe(df.describe())
        st.markdown('---')

        types = {'object': 'Categorical',
                 'int64': 'Numerical', 'float64': 'Numerical'}
        types = list(map(lambda t: types[str(t)], df.dtypes))
        st.markdown('<p class="head">Dataset Columns</p>',
                    unsafe_allow_html=True)
        for col, t in zip(df.columns, types):
            st.markdown(f"## {col}")
            cols = st.beta_columns(4)
            cols[0].markdown('#### Unique Values :')
            cols[1].markdown(f"## {df[col].unique().size}")
            cols[2].markdown('#### Type :')
            cols[3].markdown(f"## {t}")
            st.markdown("___")


def analyseTimeline():
    st.header("Timeline analysis")
    st.markdown('---')

    col1, col2 = st.beta_columns(2)

    st.markdown('---')
    st.subheader('Count of Games Released in Years')
    col1.line_chart(analysis.getYearCount())
    col2.bar_chart(analysis.getYearCount())

    col3, col4 = st.beta_columns(2)
    st.markdown('---')
    st.subheader('Count of Games Released in Years')

    col3.line_chart(analysis.getYearSum())
    col4.bar_chart(analysis.getYearSum())

    centuries = ['1980 - 1990', '1990 - 2000', '2000 - 2010', '2010 - 2020']

    popGames = {
        centuries[0]: ['PS4', 'PC', '3DS', 'XOne'],
        centuries[1]: ['PS4', 'PC', '3DS', 'XOne'],
        centuries[2]: ['PS4', 'PC', '3DS', 'XOne'],
        centuries[3]: ['PS4', 'PC', '3DS', 'XOne'],
    }

    selYear = st.selectbox(options=centuries, label="Select Year Interval")
    selPlatforms = popGames[selYear]

    st.dataframe(analysis.filterPlatform(selPlatforms))
    st.bar_chart(analysis.filterPlatform(selPlatforms))

    st.plotly_chart(plotMultiLine([analysis.getYearCount(
    ), analysis.getYearSum()], 'default', 'x', 'y', ['Count', 'Sum']), use_container_width=True)


def analysePlatform():
    st.header("Video Games Platform analysis")
    st.markdown('---')

    selRegion = st.selectbox(
        options=analysis.getRegions(),  label="Select Region")

    st.bar_chart(analysis.getPlatformSum(selRegion))

    st.line_chart(analysis.getPlatformSum(selRegion))
    st.line_chart(analysis.getPlatformCount(selRegion))
    
    data = analysis.getPlatformSum(selRegion).head(10)



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

def analyseGenre():
    st.header('Video Games Genre Analysis')
    st.markdown('---')

    selRegion = st.selectbox(
        options=analysis.getRegions(),  label="Select Region")


    st.bar_chart(analysis.getGenreSum(selRegion))

    st.line_chart(analysis.getGenreSum(selRegion))
    st.line_chart(analysis.getGenreCount(selRegion))

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
elif selOpt == choices[5]:
    analyseGenre()
