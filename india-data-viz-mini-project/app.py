import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

final_df=pd.read_csv('india.csv')
list_of_states=list(final_df['State'].unique())
list_of_states.insert(0,'Overall India')

st.sidebar.title('India Ka Data Viz')
selected_state=st.sidebar.selectbox('Select a state',list_of_states)
primary=st.sidebar.selectbox('Select Primary Parameter',sorted(list(final_df.columns[5:])))
secondary=st.sidebar.selectbox('Select Secondary Parameter',sorted(list(final_df.columns[5:])))

plot=st.sidebar.button('Plot Graph')
if plot:
    st.text('Size represent primary parameter')
    st.text('Color represents secondary parameter')
    if selected_state=='Overall India':
        # plot for india
        fig = px.scatter_mapbox(final_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=4,size_max=35,
                                mapbox_style="carto-positron",width=1200,height=700,hover_name='District')
        # Update layout to adjust size
        fig.update_layout(
            autosize=True,
            width=1700,  # Set the width
            height=700  # Set the height
        )
        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df=final_df[final_df['State']==selected_state]
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=4,size_max=35,
                                mapbox_style="carto-positron",width=1200,height=700,hover_name='District')
        # Update layout to adjust size
        fig.update_layout(
            autosize=True,
            width=1700,  # Set the width
            height=700  # Set the height
        )
        st.plotly_chart(fig,use_container_width=True)
        
