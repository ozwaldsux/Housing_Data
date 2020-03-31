#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import json
import datetime
import streamlit as st
import altair as alt
import collections
import pydeck as pdk

# Mapbox access token ########################################################

mapbox_access_token = "pk.eyJ1IjoiaGF6bGV5byIsImEiOiJjazN1cnIyaGIwN2VrM2dxZXVjd3U2bGY2In0._F8Yn8jVavOt3n6G-LarAg"






# DATA ########################################################

# df = st.cache(pd.read_csv)("test3.csv", dtype=None, encoding="unicode escape")
df = pd.read_csv("test3.csv", dtype=None, encoding="unicode escape")


df['Date'] = pd.to_datetime(df.Date)

df3 = pd.read_csv("testdf3.csv")




# Time Series ################################################


df.set_index('Date')
x = df.sort_values(by='Date')




# Prices ########################################################

max_house_prices = [(df[df['County'] == county]['Price'].max())/10**6 for county in df['County'].unique()]


county_price = df.groupby(df['County'], as_index=False)['Price'].mean()


# count values ########################################################



a = df.County.values
counttype=collections.Counter(a)
df2 = pd.DataFrame.from_dict(counttype, orient='index').reset_index()
df2 = df2.rename(columns={'index':'County', 0:'count'})


# Side Bar #######################################################


st.sidebar.subheader('Exploratory Dashboard App of Irish Housing Prices')
app_mode = st.sidebar.radio('Select mode', ('Data Exploration', 'Geoheatmap', 'Data Tables', 'Forcasting', 'Source code', 'Resources'))



if app_mode == 'Data Exploration':
# App ###########################################################
	st.title("Irish Housing Prices")

# Graphing Function - Counts #############################################################
	Counts = alt.Chart(df2, width=800, height=800).mark_bar().encode(x="County", y="count", color="County")
	st.write("Property Count By County")
	st.altair_chart(Counts)

# Graphing Function - Prices #############################################################


	Prices_mean = alt.Chart(county_price, width=800, height=800).mark_bar().encode(x="County", y="Price", color="County")
	st.write("Mean Price By County")
	st.altair_chart(Prices_mean)



# Graphing Function - Prices over time #############################################################

	Prices_ts = alt.Chart(x,width=800, height=800).mark_line().encode(x="Date", y="Price")
	st.write("Price over Time")
	st.altair_chart(Prices_ts)

# Data Tables Page #############################################################

elif app_mode == 'Data Tables':
	st.write("Raw Data Table 1")
	st.dataframe(df)
	st.write("Raw Data Table 2")
	st.dataframe(df3)



# Geoheatmap Page #############################################################

elif app_mode == 'Geoheatmap':
	layer = pdk.Layer(
    'ScatterplotLayer',     # Change the `type` positional argument here
    df3,
    get_position=['Long', 'Lat'],
    auto_highlight=True,
    get_radius=1000,          # Radius is given in meters
    get_fill_color=[180, 0, 200, 140],  # Set an RGBA value for fill
    pickable=True)
# Set the viewport location
	view_state = pdk.ViewState(
    longitude=-7.6921, latitude=53.1424, zoom=6,
     min_zoom=5, max_zoom=15, pitch=40.5, bearing=-27.36)
# Combined all of it and render a viewport
	r = pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    mapbox_key="pk.eyJ1IjoiaGF6bGV5byIsImEiOiJjazN1cnIyaGIwN2VrM2dxZXVjd3U2bGY2In0._F8Yn8jVavOt3n6G-LarAg",
    layers=[layer],
    initial_view_state=view_state,
    tooltip={"html": "<b>Price:</b> {elevationValue}", "style": {"color": "white"}},)
	st.pydeck_chart(r)


elif app_mode == 'Forcasting':
    'Add later'



elif app_mode == 'Source code':
    'Add later'



elif app_mode == 'Resources':
    'Add later'





















# # Graphing Function #############################################################



# Price_slider = st.slider('Price', 25000.0, 1550000.0, 244330.0)


























