import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="Demographix: India's Insights Hub",
    layout="wide"
)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


df =pd.read_csv('India.csv')
listOfStates=sorted(list(df['State'].unique()))
listOfStates.insert(0,'Overall India')

st.markdown("""
    <h1 style="text-align: center;">Demographix: India's Insights Hub</h1>
    """, unsafe_allow_html=True)

st.markdown("Welcome to our web app that offers a comprehensive collection of data insights through captivating visualization graphs. Our platform provides an array of features, allowing users to explore various aspects of India's demographic landscape. Dive into statistics such as literacy rates, population distribution across different religions, access to internet and electricity at the district and state levels, demographic data, age group population analysis, and sex ratio trends.")

select_state=st.selectbox('Select a State ',listOfStates)

primary = st.selectbox('Select Primary Parameter',sorted(df.columns[5:]))

secondary = st.selectbox('Select secondary  Parameter',sorted(df.columns[5:],reverse=True))

plot = st.button('Get Insights')

geojson = px.data.election_geojson()
if plot:

    st.subheader('Watch Insights')
    st.markdown("Size Represents :red[Primary Parameter], and Color Represents:blue[Secondary Parameter].")


    if select_state == 'Overall India':

        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=primary, color=secondary,  zoom=4,size_max=15,
                                    width=800, height=600,
                                    mapbox_style="carto-positron",
                                    hover_name='District',
                                    )
        fig.update_geos(fitbounds="locations")
        # fig.update_layout(mapbox_style="open-street-map")
        # fig.update_layout(mapbox_style="carto-darkmatter")

        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        st.plotly_chart(fig,use_container_width=True)

        st.subheader("State Wise Religion based Population.")

        fig = px.histogram(df, y=['Percent of Hindu Population', 'Percent of Christian Population',
                'Percent of Muslims Population', 'Percent of Buddhists Population','Percent of Sikhs Population',
                'Percent of Jains Population','Percent of people not state their Religion'],
                x=df['State'],
           barmode='group' )
        st.plotly_chart(fig,use_container_width=True)

        st.subheader("State Wise Education Qualification.")
        fig = px.histogram(df, y=['Percent of Below Primary Education', 'Percent of Secondary Education', 'Percent of Higher Education',
                                    'Percent of Graduate Education'],
                        x=df['State'],
                barmode='group' )
        st.plotly_chart(fig,use_container_width=True)

        st.subheader("Houeseholds With Internet")
        fig = px.histogram(df, x='State',y=['Households with Internet'],hover_name='State')
        st.plotly_chart(fig,use_container_width=True)

        st.subheader("Literacy Rate by State") 
        fig = px.histogram(df, y='Literacy Rate', x='State', color='District', hover_name='District')
        fig.update_layout(
            xaxis_title='State',
            yaxis_title='Literacy Rate',
            title='Literacy Rate by State'
        )
        st.plotly_chart(fig,use_container_width=True)

        st.subheader("State Wise Age Group")
        fig = px.line(df, x='District', y=['Age 0 to 29', 'Age 30 to 49', 'Age 50+'])
        st.plotly_chart(fig,use_container_width=True)

        st.subheader("Houeseholds With Electricity")
        fig = px.bar(df, x='State',y=['Households with  Electric Lighting'],hover_name='State')
        st.plotly_chart(fig,use_container_width=True)
        
        st.subheader("Sex Ratio by State")
        fig = px.histogram(df, y='Sex Ratio', x='State',color='State' ,hover_name='State')

        fig.update_layout(
            xaxis_title='State',
            yaxis_title='Sex Ratio',
            title='Sex Ratio by State'
        )
        st.plotly_chart(fig,use_container_width=True)

        st.subheader("Datagram")
        st.dataframe(df)

   




    else:
        state_df = df[df['State'] == select_state]

        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=5, size_max=35,
                                width=1200,
                                height=700,
                                mapbox_style="carto-darkmatter",
                                hover_name='District')
        # fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        st.plotly_chart(fig, use_container_width=True)
  
        st.subheader("District Wise Religion based Population.")
        fig = px.histogram(state_df, y=['Percent of Hindu Population', 'Percent of Christian Population',
                'Percent of Muslims Population', 'Percent of Buddhists Population','Percent of Sikhs Population',
                'Percent of Jains Population','Percent of people not state their Religion'],
                x=state_df['District'],
           barmode='group' )
        st.plotly_chart(fig,use_container_width=True)

        st.subheader("District Wise Education Qualification.")
        fig = px.histogram(state_df, y=['Percent of Below Primary Education', 'Percent of Secondary Education', 'Percent of Higher Education',
                               'Percent of Graduate Education'],
               #  x=finaldf['State'],
               x=state_df['District'],
           barmode='group' )
        st.plotly_chart(fig,use_container_width=True)

        st.subheader("Houeseholds With Internet")
        fig = px.line(state_df, x='District',y=['Households with Internet'],hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
        

        st.subheader("Literacy Rate by District")
        fig = px.histogram(state_df, y='Literacy Rate', x='District', color='District', hover_name='District')
        fig.update_layout(
            xaxis_title='District',
            yaxis_title='Literacy Rate',
            title='Literacy Rate by District'
        )
        st.plotly_chart(fig,use_container_width=True)

        
        st.subheader("Houeseholds With Electricity")
        fig = px.line(state_df, x='District',y=['Households with  Electric Lighting'],hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
        
        st.subheader("District Wise Age Group")
        fig = px.line(state_df, x='District', y=['Age 0 to 29', 'Age 30 to 49', 'Age 50+'])
        st.plotly_chart(fig,use_container_width=True)


        st.subheader("Sex Ratio by District")
        fig = px.histogram(state_df, y='Sex Ratio', x='District',color='District' ,hover_name='District')
        fig.update_layout(
            xaxis_title='District',
            yaxis_title='Sex Ratio',
            title='Sex Ratio by District'
        )
        st.plotly_chart(fig,use_container_width=True)



        st.subheader("Datagram")
        st.dataframe(state_df)


        


