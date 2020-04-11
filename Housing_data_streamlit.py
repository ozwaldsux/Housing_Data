#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from datetime import datetime as dt
import streamlit as st
import numpy as np
import plotly.express as px
import altair as alt
import collections
import pydeck as pdk

# Mapbox access token ########################################################

mapbox_access_token = "pk.eyJ1IjoiaGF6bGV5byIsImEiOiJjazN1cnIyaGIwN2VrM2dxZXVjd3U2bGY2In0._F8Yn8jVavOt3n6G-LarAg"






# DATA ########################################################



@st.cache(allow_output_mutation=True)
def data_load():
	load = pd.read_csv("cleaned2.csv", dtype=None, encoding="unicode escape")
	load['Date'] = pd.to_datetime(load['Date'], dayfirst=True)
	load.set_index('Date')
	load = load.sort_values(by='Date')
	load = load.loc[:, ~load.columns.str.contains('^Unnamed')]

	return load
df = data_load()




# Loading in data for plotting on Geomap ##################################

df3 = pd.read_csv("result.csv")


@st.cache(allow_output_mutation=True)
def scatter_prices():
	scatter_df = df.sample(n=100000, random_state=1)
	return scatter_df
scatter_data = scatter_prices()

# Prices ########################################################



county_price = df.groupby(df['County'], as_index=False)['Price'].mean()


# cache functions to speed up data load #############

@st.cache(allow_output_mutation=True)
def dublin():
	dub_by_year = df[df["County"] == "Dublin"].groupby(['year'], as_index=False)['Price'].mean()
	return dub_by_year


@st.cache(allow_output_mutation=True)
def cork():
	cork_by_year = df[df["County"] == "Cork"].groupby(['year'], as_index=False)['Price'].mean()
	return cork_by_year

@st.cache(allow_output_mutation=True)
def Kildare():
	kildare_by_year = df[df["County"] == "Kildare"].groupby(['year'], as_index=False)['Price'].mean()
	return kildare_by_year

@st.cache(allow_output_mutation=True)
def Wicklow():
	wicklow_by_year = df[df["County"] == "Wicklow"].groupby(['year'], as_index=False)['Price'].mean()
	return wicklow_by_year

@st.cache(allow_output_mutation=True)
def Meath():
	meath_by_year = df[df["County"] == "Meath"].groupby(['year'], as_index=False)['Price'].mean()
	return meath_by_year

@st.cache(allow_output_mutation=True)
def Limerick():
	Limerick_by_year = df[df["County"] == "Limerick"].groupby(['year'], as_index=False)['Price'].mean()
	return Limerick_by_year

@st.cache(allow_output_mutation=True)
def Longford():
	Longford_by_year = df[df["County"] == "Longford"].groupby(['year'], as_index=False)['Price'].mean()
	return Longford_by_year


@st.cache(allow_output_mutation=True)
def Monaghan():
	Monaghan_by_year = df[df["County"] == "Monaghan"].groupby(['year'], as_index=False)['Price'].mean()
	return Monaghan_by_year


@st.cache(allow_output_mutation=True)
def Galway():
	Galway_by_year = df[df["County"] == "Galway"].groupby(['year'], as_index=False)['Price'].mean()
	return Galway_by_year


@st.cache(allow_output_mutation=True)
def Wexford():
	Wexford_by_year = df[df["County"] == "Wexford"].groupby(['year'], as_index=False)['Price'].mean()
	return Wexford_by_year


@st.cache(allow_output_mutation=True)
def Kerry():
	Kerry_by_year = df[df["County"] == "Kerry"].groupby(['year'], as_index=False)['Price'].mean()
	return Kerry_by_year

@st.cache(allow_output_mutation=True)
def Tipperary():
	Tipperary_by_year = df[df["County"] == "Tipperary"].groupby(['year'], as_index=False)['Price'].mean()
	return Tipperary_by_year


@st.cache(allow_output_mutation=True)
def Louth():
	Louth_by_year = df[df["County"] == "Louth"].groupby(['year'], as_index=False)['Price'].mean()
	return Louth_by_year


@st.cache(allow_output_mutation=True)
def Waterford():
	Waterford_by_year = df[df["County"] == "Waterford"].groupby(['year'], as_index=False)['Price'].mean()
	return Waterford_by_year



@st.cache(allow_output_mutation=True)
def Donegal():
	Donegal_by_year = df[df["County"] == "Donegal"].groupby(['year'], as_index=False)['Price'].mean()
	return Donegal_by_year



@st.cache(allow_output_mutation=True)
def Mayo():
	Mayo_by_year = df[df["County"] == "Mayo"].groupby(['year'], as_index=False)['Price'].mean()
	return Mayo_by_year


@st.cache(allow_output_mutation=True)
def Clare():
	Clare_by_year = df[df["County"] == "Clare"].groupby(['year'], as_index=False)['Price'].mean()
	return Clare_by_year


@st.cache(allow_output_mutation=True)
def Westmeath():
	Westmeath_by_year = df[df["County"] == "Westmeath"].groupby(['year'], as_index=False)['Price'].mean()
	return Westmeath_by_year



@st.cache(allow_output_mutation=True)
def Cavan():
	Cavan_by_year = df[df["County"] == "Cavan"].groupby(['year'], as_index=False)['Price'].mean()
	return Cavan_by_year


@st.cache(allow_output_mutation=True)
def Sligo():
	Sligo_by_year = df[df["County"] == "Sligo"].groupby(['year'], as_index=False)['Price'].mean()
	return Sligo_by_year


@st.cache(allow_output_mutation=True)
def Roscommon():
	Roscommon_by_year = df[df["County"] == "Roscommon"].groupby(['year'], as_index=False)['Price'].mean()
	return Roscommon_by_year


@st.cache(allow_output_mutation=True)
def Laois():
	Laois_by_year = df[df["County"] == "Laois"].groupby(['year'], as_index=False)['Price'].mean()
	return Laois_by_year


@st.cache(allow_output_mutation=True)
def Kilkenny():
	Kilkenny_by_year = df[df["County"] == "Kilkenny"].groupby(['year'], as_index=False)['Price'].mean()
	return Kilkenny_by_year


@st.cache(allow_output_mutation=True)
def Offaly():
	Offaly_by_year = df[df["County"] == "Offaly"].groupby(['year'], as_index=False)['Price'].mean()
	return Offaly_by_year

@st.cache(allow_output_mutation=True)
def Carlow():
	Carlow_by_year = df[df["County"] == "Carlow"].groupby(['year'], as_index=False)['Price'].mean()
	return Carlow_by_year  
       
@st.cache(allow_output_mutation=True)
def Leitrim():
	Leitrim_by_year = df[df["County"] == "Leitrim"].groupby(['year'], as_index=False)['Price'].mean()
	return Leitrim_by_year    
     
           
@st.cache(allow_output_mutation=True)
def by_year():
	year_group = df.groupby(['year'], as_index=False)['Price'].mean()
	return year_group






########################################################################################

@st.cache(allow_output_mutation=True)
def dublin_data():
	dub_box = df[df['County'] == "Dublin"]
	return dub_box

@st.cache(allow_output_mutation=True)
def cork_data():
	cork_box = df[df["County"] == "Cork"]
	return cork_box

@st.cache(allow_output_mutation=True)
def Kildare_data():
	kildare_box = df[df["County"] == "Kildare"]
	return kildare_box

@st.cache(allow_output_mutation=True)
def Wicklow_data():
	wicklow_box = df[df["County"] == "Wicklow"]
	return wicklow_box

@st.cache(allow_output_mutation=True)
def Meath_data():
	meath_box = df[df["County"] == "Meath"]
	return meath_box

@st.cache(allow_output_mutation=True)
def Limerick_data():
	Limerick_box = df[df["County"] == "Limerick"]
	return Limerick_box

@st.cache(allow_output_mutation=True)
def Longford_data():
	Longford_box = df[df["County"] == "Longford"]
	return Longford_box


@st.cache(allow_output_mutation=True)
def Monaghan_data():
	Monaghan_box = df[df["County"] == "Monaghan"]
	return Monaghan_box


@st.cache(allow_output_mutation=True)
def Galway_data():
	Galway_box = df[df["County"] == "Galway"]
	return Galway_box


@st.cache(allow_output_mutation=True)
def Wexford_data():
	Wexford_box = df[df["County"] == "Wexford"]
	return Wexford_box


@st.cache(allow_output_mutation=True)
def Kerry_data():
	Kerry_box = df[df["County"] == "Kerry"]
	return Kerry_box

@st.cache(allow_output_mutation=True)
def Tipperary_data():
	Tipperary_box = df[df["County"] == "Tipperary"]
	return Tipperary_box


@st.cache(allow_output_mutation=True)
def Louth_data():
	Louth_box = df[df["County"] == "Louth"]
	return Louth_box


@st.cache(allow_output_mutation=True)
def Waterford_data():
	Waterford_box = df[df["County"] == "Waterford"]
	return Waterford_box



@st.cache(allow_output_mutation=True)
def Donegal_data():
	Donegal_box = df[df["County"] == "Donegal"]
	return Donegal_box



@st.cache(allow_output_mutation=True)
def Mayo_data():
	Mayo_box = df[df["County"] == "Mayo"]
	return Mayo_box


@st.cache(allow_output_mutation=True)
def Clare_data():
	Clare_box = df[df["County"] == "Clare"]
	return Clare_box


@st.cache(allow_output_mutation=True)
def Westmeath_data():
	Westmeath_box = df[df["County"] == "Westmeath"]
	return Westmeath_box



@st.cache(allow_output_mutation=True)
def Cavan_data():
	Cavan_box = df[df["County"] == "Cavan"]
	return Cavan_box


@st.cache(allow_output_mutation=True)
def Sligo_data():
	Sligo_box = df[df["County"] == "Sligo"]
	return Sligo_box


@st.cache(allow_output_mutation=True)
def Roscommon_data():
	Roscommon_box = df[df["County"] == "Roscommon"]
	return Roscommon_box


@st.cache(allow_output_mutation=True)
def Laois_data():
	Laois_box = df[df["County"] == "Laois"]
	return Laois_box


@st.cache(allow_output_mutation=True)
def Kilkenny_data():
	Kilkenny_box = df[df["County"] == "Kilkenny"]
	return Kilkenny_box


@st.cache(allow_output_mutation=True)
def Offaly_data():
	Offaly_box = df[df["County"] == "Offaly"]
	return Offaly_box

@st.cache(allow_output_mutation=True)
def Carlow_data():
	Carlow_box = df[df["County"] == "Carlow"]
	return Carlow_box  
       
@st.cache(allow_output_mutation=True)
def Leitrim_data():
	Leitrim_box = df[df["County"] == "Leitrim"]
	return Leitrim_box    

year_price = by_year()
Dublin_price = dublin()
Cork_price = cork()
Kildare_price = Kildare()
Wicklow_price = Wicklow()
Meath_price = Meath()
Limerick_price  = Limerick()
Wexford_price = Wexford()    
Wicklow_price = Wicklow()    
Kerry_price = Kerry()    
Tipperary_price = Tipperary()  
Louth_price = Louth() 
Waterford_price = Waterford()  
Donegal_price = Donegal()   
Mayo_price = Mayo()   
Clare_price = Clare()    
Westmeath_price = Westmeath()    
Cavan_price = Cavan()   
Sligo_price = Sligo()     
Roscommon_price = Roscommon()   
Laois_price = Laois()    
Kilkenny_price = Kilkenny()  
Offaly_price = Offaly()    
Carlow_price = Carlow()    
Leitrim_price = Leitrim()    
Monaghan_price = Monaghan()    
Longford_price = Longford()





Dublin_boxplot = dublin_data()
Cork_boxplot = cork_data()
Kildare_boxplot = Kildare_data()
Wicklow_boxplot = Wicklow_data()
Meath_boxplot = Meath_data()
Limerick_boxplot  = Limerick_data()
Wexford_boxplot = Wexford_data()    
Wicklow_boxplot = Wicklow_data()    
Kerry_boxplot = Kerry_data()    
Tipperary_boxplot = Tipperary_data()  
Louth_boxplot = Louth_data() 
Waterford_boxplot = Waterford_data()  
Donegal_boxplot = Donegal_data()   
Mayo_boxplot = Mayo_data()   
Clare_boxplot = Clare_data()    
Westmeath_boxplot = Westmeath_data()    
Cavan_boxplot = Cavan_data()   
Sligo_boxplot = Sligo_data()     
Roscommon_boxplot = Roscommon_data()   
Laois_boxplot = Laois_data()    
Kilkenny_boxplot = Kilkenny_data()  
Offaly_boxplot = Offaly_data()    
Carlow_boxplot = Carlow_data()    
Leitrim_boxplot = Leitrim_data()    
Monaghan_boxplot = Monaghan_data()    
Longford_boxplot = Longford_data()












# count values ########################################################



a = df.County.values
counttype=collections.Counter(a)
df2 = pd.DataFrame.from_dict(counttype, orient='index').reset_index()
df2 = df2.rename(columns={'index':'County', 0:'count'})


# Side Bar #######################################################


st.sidebar.header('Exploratory Dashboard App of Irish Housing Prices')
app_mode = st.sidebar.radio('Select mode', ('Home', 'Geoheatmap', 'Data Tables', 'Forcasting', 'Notebook', 'Resources'))
st.sidebar.subheader("Select Chart: ")



if app_mode == 'Home':
# App ###########################################################
	st.title("Irish Housing Prices")
	st.header("Welcome to my streamlit app exploring Irish housing prices over the last decade!")
	st.write("*Disclaimer* Dataset has been cleaned and outliers have been removed.")

# Graphing Function - Counts #############################################################
	Property_Count_County = st.sidebar.checkbox("Property Count By County")
	if Property_Count_County:
		Counts = alt.Chart(df2, width=800, height=800).mark_bar().encode(x="County", y="count", color="County")
		st.header("Property Count By County")
		st.write("This chart shows the total number of properties sold by County")
		st.altair_chart(Counts)

# Graphing Function - Prices #############################################################

	Price_Mean_county = st.sidebar.checkbox("Mean Price By County")
	if Price_Mean_county:
		Prices_mean = alt.Chart(county_price, width=800, height=800).mark_bar().encode(x="County", y="Price", color="County")
		st.header("Mean Price By County")
		st.write("This chart shows the mean price of properties sold by County between 2010-2020")
		st.altair_chart(Prices_mean)

#Scatter Plot Graph #######################################################

	Price_scatterplot = st.sidebar.checkbox("Prices Over Past Decade")
	if Price_scatterplot:
		st.header("Prices Over Past Decade")
		st.write("This chart shows a sample distribution of prices over the past decade")
		alt.data_transformers.disable_max_rows()
		prices_scatter = alt.Chart(scatter_data, width=800, height=800).mark_circle(size=60).encode(x='Date:T', y='Price', color='Price', tooltip=['Date:T', 'Price', 'County'])
		st.altair_chart(prices_scatter)


# Graphing Function - Prices over time #############################################################


	Price_trend = st.sidebar.checkbox("Price Trend Line Over Decade By County")
	if Price_trend:
		st.header("Price Trend Over Decade By County")
		st.write("These charts display the price trend over time by individual county and also nationwide.")
		price_over_time = st.selectbox("Select County: ", ("Nationwide", "Dublin", "Cork","Kildare","Wicklow","Meath", "Limerick","Wexford", "Wicklow","Kerry","Tipperary","Louth","Waterford","Donegal", "Mayo","Clare","Westmeath","Cavan","Sligo","Roscommon", "Laois", "Kilkenny ", "Offaly", "Carlow", "Leitrim", "Monaghan", "Longford"))

		if price_over_time == "Nationwide":
			by_county = alt.Chart(year_price,width=800, height=800).mark_line().encode(x="year:O", y="mean(Price)", tooltip=["mean(Price)"])
			st.write("Nationwide Average Price Per Year")
			st.altair_chart(by_county)


		elif price_over_time == "Dublin":
			Dublin= alt.Chart(Dublin_price,width=800, height=800).mark_line().encode(x="year:O", y="Price").configure_mark(opacity=1, color='black') 
			st.write("Dublin Average Price Per Year") 
			st.altair_chart(Dublin)	

		elif price_over_time == "Cork":
			Cork= alt.Chart(Cork_price,width=800, height=800).mark_line().encode(x="year:O", y="Price").configure_mark(opacity=1, color='cyan') 
			st.write("Cork Average Price Per Year") 
			st.altair_chart(Cork)


		elif price_over_time == "Kildare":
			Kildare= alt.Chart(Kildare_price,width=800, height=800).mark_line().encode(x="year:O", y="Price").configure_mark(opacity=1, color='brown')
			st.write("Kildare Average Price Per Year") 
			st.altair_chart(Kildare)


		elif price_over_time == "Galway":
			Galway= alt.Chart(Galway_price,width=800, height=800).mark_line().encode(x="year:O", y="Price").configure_mark(opacity=1, color='purple') 
			st.write("Galway Average Price Per Year") 
			st.altair_chart(Galway)


		elif price_over_time == "Meath":
			Meath= alt.Chart(Meath_price,width=800, height=800).mark_line().encode(x="year:O", y="Price").configure_mark(opacity=1, color='purple') 
			st.write("Meath Average Price Per Year") 
			st.altair_chart(Meath)


		elif price_over_time == "Limerick":
			Limerick= alt.Chart(Limerick_price,width=800, height=800).mark_line().encode(x="year:O", y="Price").configure_mark(opacity=1, color='red') 
			st.write("Limerick Average Price Per Year") 
			st.altair_chart(Limerick)


		elif price_over_time == "Wexford":
			Wexford= alt.Chart(Wexford_price,width=800, height=800).mark_line().encode(x="year:O", y="Price").configure_mark(opacity=1, color='green') 
			st.write("Wexford Average Price Per Year") 
			st.altair_chart(Wexford)


		elif price_over_time == "Wicklow":
			Wicklow= alt.Chart(Wicklow_price,width=800, height=800).mark_line().encode(x="year:O", y="Price").configure_mark(opacity=1, color='black') 
			st.write("Wicklow Average Price Per Year") 
			st.altair_chart(Wicklow)


		elif price_over_time == "Kerry":
			Kerry= alt.Chart(Kerry_price,width=800, height=800).mark_line().encode(x="year:O", y="Price").configure_mark(opacity=1, color='pink') 
			st.write("Kerry Average Price Per Year") 
			st.altair_chart(Kerry)


		elif price_over_time == "Tipperary":
			Tipperary= alt.Chart(Tipperary_price,width=800, height=800).mark_line().encode(x="year:O", y="Price").configure_mark(opacity=1, color='orange') 
			st.write("Tipperary Average Price Per Year") 
			st.altair_chart(Tipperary)


		elif price_over_time == "Louth":
			Louth= alt.Chart(Louth_price,width=800, height=800).mark_line().encode(x="year:O", y="Price").configure_mark(opacity=1, color='green') 
			st.write("Louth Average Price Per Year") 
			st.altair_chart(Louth)


		elif price_over_time == "Waterford":
			Waterford= alt.Chart(Waterford_price,width=800, height=800).mark_line().encode(x="year:O", y="Price").configure_mark(opacity=1, color='red') 
			st.write("Waterford Average Price Per Year") 
			st.altair_chart(Waterford)


		elif price_over_time == "Donegal":
			Donegal= alt.Chart(Donegal_price,width=800, height=800).mark_line().encode(x="year:O", y="Price").configure_mark(opacity=1, color='green') 
			st.write("Donegal Average Price Per Year") 
			st.altair_chart(Donegal)


		elif price_over_time == "Mayo":
			Mayo= alt.Chart(Mayo_price,width=800, height=800).mark_line().encode(x="year:O", y="Price").configure_mark(opacity=1, color='black') 
			st.write("Mayo Average Price Per Year") 
			st.altair_chart(Mayo)


		elif price_over_time == "Clare":
			Clare= alt.Chart(Clare_price,width=800, height=800).mark_line().encode(x="year:O", y="Price").configure_mark(opacity=1, color='red') 
			st.write("Clare Average Price Per Year") 
			st.altair_chart(Clare)


		elif price_over_time == "Westmeath":
			Westmeath= alt.Chart(Westmeath_price,width=800, height=800).mark_line().encode(x="year:O", y="Price").configure_mark(opacity=1, color='cyan') 
			st.write("Westmeath Average Price Per Year") 
			st.altair_chart(Westmeath)


		elif price_over_time == "Cavan":
			Cavan= alt.Chart(Cavan_price,width=800, height=800).mark_line().encode(x="year:O", y="Price").configure_mark(opacity=1, color='orange') 
			st.write("Cavan Average Price Per Year") 
			st.altair_chart(Cavan)


		elif price_over_time == "Sligo":
			Sligo= alt.Chart(Sligo_price,width=800, height=800).mark_line().encode(x="year:O", y="Price").configure_mark(opacity=1, color='blue') 
			st.write("Sligo Average Price Per Year") 
			st.altair_chart(Sligo)

		elif price_over_time == "Roscommon":
			Roscommon= alt.Chart(Roscommon_price,width=800, height=800).mark_line().encode(x="year:O", y="Price").configure_mark(opacity=1, color='grey') 
			st.write("Roscommon Average Price Per Year") 
			st.altair_chart(Roscommon)

		elif price_over_time == "Laois":
			Laois= alt.Chart(Laois_price,width=800, height=800).mark_line().encode(x="year:O", y="Price").configure_mark(opacity=1, color='blue') 
			st.write("Laois Average Price Per Year") 
			st.altair_chart(Laois)

		elif price_over_time == "Kilkenny":
			Kilkenny= alt.Chart(Kilkenny_price,width=800, height=800).mark_line().encode(x="year:O", y="Price").configure_mark(opacity=1, color='grey') 
			st.write("Kilkenny Average Price Per Year") 
			st.altair_chart(Kilkenny)

		elif price_over_time == "Offaly":
			Offaly= alt.Chart(Offaly_price,width=800, height=800).mark_line().encode(x="year:O", y="Price").configure_mark(opacity=1, color='brown') 
			st.write("Offaly Average Price Per Year") 
			st.altair_chart(Offaly)

		elif price_over_time == "Carlow":
			Carlow= alt.Chart(Carlow_price,width=800, height=800).mark_line().encode(x="year:O", y="Price").configure_mark(opacity=1, color='blue') 
			st.write("Carlow Average Price Per Year") 
			st.altair_chart(Carlow)

		elif price_over_time == "Leitrim":
			Leitrim= alt.Chart(Leitrim_price,width=800, height=800).mark_line().encode(x="year:O", y="Price").configure_mark(opacity=1, color='orange') 
			st.write("Leitrim Average Price Per Year") 
			st.altair_chart(Leitrim)

		elif price_over_time == "Monaghan":
			Monaghan= alt.Chart(Monaghan_price,width=800, height=800).mark_line().encode(x="year:O", y="Price").configure_mark(opacity=1, color='pink') 
			st.write("Monaghan Average Price Per Year") 
			st.altair_chart(Monaghan)

		elif price_over_time == "Longford":
			Longford= alt.Chart(Longford_price,width=800, height=800).mark_line().encode(x="year:O", y="Price").configure_mark(opacity=1, color='cyan') 
			st.write("Longford Average Price Per Year") 
			st.altair_chart(Longford)



#  Boxplots ######################################################################
	
	Price_distribution_county = st.sidebar.checkbox("Price Distribution By County")
	if Price_distribution_county:
		st.header("Price Distribution By County")
		st.write("These charts display the price distribution by county over the last decade.")
		Boxplot = st.selectbox("Select County: ", ("Dublin", "Cork","Kildare","Wicklow","Meath", "Limerick","Wexford", "Wicklow","Kerry","Tipperary","Louth","Waterford","Donegal", "Mayo","Clare","Westmeath","Cavan","Sligo","Roscommon", "Laois", "Kilkenny ", "Offaly", "Carlow", "Leitrim", "Monaghan", "Longford"))


		if Boxplot == "Dublin":
			Dublin = alt.Chart(Dublin_boxplot, width=800, height=800).mark_boxplot().encode(x='County:O', y='Price:Q').configure_mark(opacity=1, color='black') 
			st.write("Dublin Price Range") 
			st.altair_chart(Dublin)




		elif Boxplot == "Cork":
			Cork= alt.Chart(Cork_boxplot,width=800, height=800).mark_boxplot().encode(x='County:O', y='Price:Q').configure_mark(opacity=1, color='cyan') 
			st.write("Cork Price Range") 
			st.altair_chart(Cork)


		elif Boxplot == "Kildare":
			Kildare= alt.Chart(Kildare_boxplot,width=800, height=800).mark_boxplot().encode(x='County:O', y='Price:Q').configure_mark(opacity=1, color='brown')
			st.write("Kildare Price Range") 
			st.altair_chart(Kildare)


		elif Boxplot == "Galway":
			Galway= alt.Chart(Galway_boxplot,width=800, height=800).mark_boxplot().encode(x='County:O', y='Price:Q').configure_mark(opacity=1, color='purple') 
			st.write("Galway Price Range") 
			st.altair_chart(Galway)


		elif Boxplot == "Meath":
			Meath= alt.Chart(Meath_boxplot,width=800, height=800).mark_boxplot().encode(x='County:O', y='Price:Q').configure_mark(opacity=1, color='purple') 
			st.write("Meath Price Range") 
			st.altair_chart(Meath)


		elif Boxplot == "Limerick":
			Limerick= alt.Chart(Limerick_boxplot,width=800, height=800).mark_boxplot().encode(x='County:O', y='Price:Q').configure_mark(opacity=1, color='red') 
			st.write("Limerick Price Range") 
			st.altair_chart(Limerick)


		elif Boxplot == "Wexford":
			Wexford= alt.Chart(Wexford_boxplot,width=800, height=800).mark_boxplot().encode(x='County:O', y='Price:Q').configure_mark(opacity=1, color='green') 
			st.write("Wexford Price Range") 
			st.altair_chart(Wexford)


		elif Boxplot == "Wicklow":
			Wicklow= alt.Chart(Wicklow_boxplot,width=800, height=800).mark_boxplot().encode(x='County:O', y='Price:Q').configure_mark(opacity=1, color='black') 
			st.write("Wicklow Price Range") 
			st.altair_chart(Wicklow)


		elif Boxplot == "Kerry":
			Kerry= alt.Chart(Kerry_boxplot,width=800, height=800).mark_boxplot().encode(x='County:O', y='Price:Q').configure_mark(opacity=1, color='pink') 
			st.write("Kerry Price Range") 
			st.altair_chart(Kerry)


		elif Boxplot == "Tipperary":
			Tipperary= alt.Chart(Tipperary_boxplot,width=800, height=800).mark_boxplot().encode(x='County:O', y='Price:Q').configure_mark(opacity=1, color='orange') 
			st.write("Tipperary Price Range") 
			st.altair_chart(Tipperary)


		elif Boxplot == "Louth":
			Louth= alt.Chart(Louth_boxplot,width=800, height=800).mark_boxplot().encode(x='County:O', y='Price:Q').configure_mark(opacity=1, color='green') 
			st.write("Louth Price Range") 
			st.altair_chart(Louth)


		elif Boxplot == "Waterford":
			Waterford= alt.Chart(Waterford_boxplot,width=800, height=800).mark_boxplot().encode(x='County:O', y='Price:Q').configure_mark(opacity=1, color='red') 
			st.write("Waterford Price Range") 
			st.altair_chart(Waterford)


		elif Boxplot == "Donegal":
			Donegal= alt.Chart(Donegal_boxplot,width=800, height=800).mark_boxplot().encode(x='County:O', y='Price:Q').configure_mark(opacity=1, color='green') 
			st.write("Donegal Price Range") 
			st.altair_chart(Donegal)


		elif Boxplot == "Mayo":
			Mayo= alt.Chart(Mayo_boxplot,width=800, height=800).mark_boxplot().encode(x='County:O', y='Price:Q').configure_mark(opacity=1, color='black') 
			st.write("Mayo Price Range") 
			st.altair_chart(Mayo)


		elif Boxplot == "Clare":
			Clare= alt.Chart(Clare_boxplot,width=800, height=800).mark_boxplot().encode(x='County:O', y='Price:Q').configure_mark(opacity=1, color='red') 
			st.write("Clare Price Range") 
			st.altair_chart(Clare)


		elif Boxplot == "Westmeath":
			Westmeath= alt.Chart(Westmeath_boxplot,width=800, height=800).mark_boxplot().encode(x='County:O', y='Price:Q').configure_mark(opacity=1, color='cyan') 
			st.write("Westmeath Price Range") 
			st.altair_chart(Westmeath)


		elif Boxplot == "Cavan":
			Cavan= alt.Chart(Cavan_boxplot,width=800, height=800).mark_boxplot().encode(x='County:O', y='Price:Q').configure_mark(opacity=1, color='orange') 
			st.write("Cavan Price Range") 
			st.altair_chart(Cavan)


		elif Boxplot == "Sligo":
			Sligo= alt.Chart(Sligo_boxplot,width=800, height=800).mark_boxplot().encode(x='County:O', y='Price:Q').configure_mark(opacity=1, color='blue') 
			st.write("Sligo Price Range") 
			st.altair_chart(Sligo)

		elif Boxplot == "Roscommon":
			Roscommon= alt.Chart(Roscommon_boxplot,width=800, height=800).mark_boxplot().encode(x='County:O', y='Price:Q').configure_mark(opacity=1, color='grey') 
			st.write("Roscommon Price Range") 
			st.altair_chart(Roscommon)

		elif Boxplot == "Laois":
			Laois= alt.Chart(Laois_boxplot,width=800, height=800).mark_boxplot().encode(x='County:O', y='Price:Q').configure_mark(opacity=1, color='blue') 
			st.write("Laois Price Range") 
			st.altair_chart(Laois)

		elif Boxplot == "Kilkenny":
			Kilkenny= alt.Chart(Kilkenny_boxplot,width=800, height=800).mark_boxplot().encode(x='County:O', y='Price:Q').configure_mark(opacity=1, color='grey') 
			st.write("Kilkenny Price Range") 
			st.altair_chart(Kilkenny)

		elif Boxplot == "Offaly":
			Offaly= alt.Chart(Offaly_boxplot,width=800, height=800).mark_boxplot().encode(x='County:O', y='Price:Q').configure_mark(opacity=1, color='brown') 
			st.write("Offaly Price Range") 
			st.altair_chart(Offaly)

		elif Boxplot == "Carlow":
			Carlow= alt.Chart(Carlow_boxplot,width=800, height=800).mark_boxplot().encode(x='County:O', y='Price:Q').configure_mark(opacity=1, color='blue') 
			st.write("Carlow Price Range") 
			st.altair_chart(Carlow)

		elif Boxplot == "Leitrim":
			Leitrim= alt.Chart(Leitrim_boxplot,width=800, height=800).mark_boxplot().encode(x='County:O', y='Price:Q').configure_mark(opacity=1, color='orange') 
			st.write("Leitrim Price Range") 
			st.altair_chart(Leitrim)

		elif Boxplot == "Monaghan":
			Monaghan= alt.Chart(Monaghan_boxplot,width=800, height=800).mark_boxplot().encode(x='County:O', y='Price:Q').configure_mark(opacity=1, color='pink') 
			st.write("Monaghan Price Range") 
			st.altair_chart(Monaghan)

		elif Boxplot == "Longford":
			Longford= alt.Chart(Longford_boxplot,width=800, height=800).mark_boxplot().encode(x='County:O', y='Price:Q').configure_mark(opacity=1, color='cyan') 
			st.write("Longford Price Range") 
			st.altair_chart(Longford)






# Histograme Distribution ###########################################################################

	Price_distribution = st.sidebar.checkbox("Price Distribution By Count")
	if Price_distribution:
		st.header("Price Distribution By Count")
		st.write("You can select a price range to visualise the distribution by selecting each end of the slider. Note: The wider the range, the longer the loading time.")
		values = st.slider("Price", float(df.Price.min()),
		2625000., (5030., 300000.))
		f = px.histogram(df.query(f"Price.between{values}"), x="Price", nbins=15, title="Price distribution")
		f.update_xaxes(title="Price")
		f.update_yaxes(title="No. of listings")
		st.plotly_chart(f)





# Data Tables Page #############################################################

elif app_mode == 'Data Tables':
	st.title("Raw Data Tables")
	st.write("Currently, streamlit does not support searchable datatables to my knowledge. However, as soon as this feature becomes available, I will be adding it.")


		
	st.write("Raw Data Table 1")
	st.write(df)

	st.write("Raw Data Table 2")
	st.dataframe(df3)



# Geoheatmap Page #############################################################

elif app_mode == 'Geoheatmap':
	st.title("Average Housing Prices By County 2019")

	st.write("This map visualises average housing prices by each county for 2019. Each of the markers is scaled to price. As we can see, Dublin, Kildare, Meath and Wicklow are the largest and therefore have the highest average house prices.")




	layer = pdk.Layer(
    'ScatterplotLayer',     # Change the `type` positional argument here
    df3,
    get_position=['Long', 'Lat'],
    auto_highlight=True,
    get_radius="Price/10",          # Radius is given in meters
    get_fill_color=[100, 0, 120, 140],  # Set an RGBA value for fill
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
    tooltip={"html": "<b>Price (€):</b> {Price}<br> <b>Address:</b> {County}", "style": {"color": "white"}}, )
	st.pydeck_chart(r)


	
# Geoheatmap Page #############################################################

elif app_mode == 'Forcasting':
    st.title('Coming Soon')
    st.write("I am currently pausing on any predictive algoirithm, as it is likley these predictions will be inaccurate due to the economic effects of Covid-19, which the current dataset will not take account of. However as new data emerges, the impact will likely begin to show. My own opinion is that we will see prices fall as unemployment rises, but it is unclear as to the extent that this will occur. It may also be possible to combine other datasets which could indicate consumer demand.")
    st.write("If anyone has done any work regarding this and would like to share their ideas or discuss further, my email is hazleyo @ protonmail.com")


elif app_mode == 'Notebook':
    st.title('Irish_Housing_Prices.ipynb')
    st.header('')
    "Import our libraries and setup our intial dataframe. Encoding is set to latin as there appears to be some non Utf-8 characters (I couldn't find them but maybe someone will correct me). "
    codesnippet_1 = (
		'''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/content/PPR-ALL.csv", encoding="Latin", thousands=',')
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df.head()
		''')
    st.code(codesnippet_1, language='python')
    st.write("Next check our dtypes and begin construction of a data quality report")
    codesnippet_2 = ('''df.dtypes
df.shape ''')
    st.code(codesnippet_2, language='python')
    st.write("Next we want to check the summary amount of missing values. As we can see, the dataset is good quality, so there is not much cleanup required. That being said, we will still want to drop columns which are missing significant amounts of values which in this case appears to be ""Postal Code"" and ""Property Size Description"".")
    codesnippet_3 = ('''df.isnull().sum()''') 
    st.code(codesnippet_3, language='python')   
    st.write("Drop unneeded columns and we want to remove the euro sign from all our entries in the 'Price' column. We do this by applying the following lambda function. We then set the column names to how we which them to appear and set the date as the index.")
    codesnippet_4 = ('''df.drop(["Postal Code","Not Full Market Price", "VAT Exclusive", 
    	"Property Size Description", "Description of Property"], axis=1, inplace=True)
df['Price ()'] = df["Price ()"].apply(lambda x: ''.join([" " if ord(i) < 32 or ord(i) > 126 else i for i in x]))
df.columns = ['Date','Address','County','Price']
df.head(10) ''')
    st.code(codesnippet_4, language='python')
    st.write("Next, we want to remove the commas from our 'Price' column and convert the dtype to float.")
    codesnippet_5 = ('''df['Price'] = pd.to_numeric(df['Price'].str.replace(',', ''), 
    	errors='coerce', downcast='integer')

df['Date'] = pd.to_datetime(df.Date)''')
    st.code(codesnippet_5, language='python')    
    st.write("Then Convert the Price column to integers & convert the Address dtype to string")
    codesnippet_6 = ('''df['Price'] = df['Price'].astype(int)
    	df['Address'] = df['Address'].astype(str)
df.dtypes    ''')
    st.code(codesnippet_6, language='python')
    st.write("Now we remove outliers ")
    codesnippet_7 = ('''from scipy import stats

def drop_numerical_outliers(df, z_thresh=3):
    # Constrains will contain `True` or `False` depending on if it is a value below the threshold.
    constrains = df.select_dtypes(include=[np.number]) \
        .apply(lambda x: np.abs(stats.zscore(x)) < z_thresh, result_type='reduce') \
        .all(axis=1)
    # Drop (inplace) values set to be rejected
    df.drop(df.index[~constrains], inplace=True)
    drop_numerical_outliers(df)
    ''')
    st.code(codesnippet_7, language='python')
    st.write("Now we want to prepare the data for the geomap. After many iterations and trials, I decided to display average prices by county for 2019")
    codesnippet_8 = ('''import datetime as dt

county_price = df[df['Date'].dt.year == 2019]
county_price = county_price.groupby(county_price['County'], as_index=False)['Price'].mean()
county_price["Price"] = county_price["Price"].astype(int)
county_price.head(26) ''')
    st.code(codesnippet_8, language='python')
    st.write("Next we need to load our ""Counties.csv"". This is list of counties and their coordinates which we will use to plot on the map alongside the average prices for 2019.")
    codesnippet_9 = ('''df2 = pd.read_csv("/content/counties.csv")
df2 = df2.loc[:, ~df2.columns.str.contains('^Unnamed')]
df2.head()''')
    st.code(codesnippet_9, language='python')
    st.write("After trial and error, I notice that the County field in PPR-all.csv have a space at the end of them. This prevented the two data frames from being merged. To ensure merging was successful we simply replace the space with an empty string. We then want to convert the two dataframe columns to strings so there are no other compatibility issues when merging.")
    codesnippet_10 = ('''df2.County = df2.County.str.replace(' ', '')
county_price.County = county_price.County.str.replace(' ', '')
df2["County"] = df2["County"].astype(str)
county_price["County"] = county_price["County"].astype(str) ''')
    st.code(codesnippet_10, language='python')
    st.write("Next, we merge on 'County'")
    codesnippet_11 = ('''result = pd.merge(county_price, df2[["County", "Lat", "Long"]], on="County", how="left") ''')
    st.code(codesnippet_11, language='python')
    st.write("Now, we reorder the columns. Pydeck, which is the library used to visualise the data, must receive the longtitude value first, then the latitude and then the remaining values.")
    codesnippet_12 = ('''result = result[["Long", "Lat", "County", "Price"]]

result.head() ''')
    st.code(codesnippet_12, language='python')
    st.write("Finally we export our dataframes as csv so that our programme can read them from our git repo.")
    codesnippet_13 = ('''result.to_csv("/content/result.csv", index=False)
df.to_csv("/content/drive/My Drive/PPR_ALL_Clean", index=False)     ''')
    st.code(codesnippet_13, language='python')
    st.write("We can also visualise our data to check the distribution as follows")
    codesnippet_14 = ('''df.plot(x='Date', y='Price') 
df.hist(column="Price", bins=25, log=True)
df.boxplot(column=['Price'], by=['County'])
df.plot.scatter(x='Date', y='Price', c='Price', colormap='viridis')''')
    st.code(codesnippet_14, language='python')




elif app_mode == 'Resources':
    st.title('Resource List:')
    st.write('https://www.propertypriceregister.ie/')
    st.write('https://www.shanelynn.ie/the-irish-property-price-register-geocoded-to-small-areas/')
    st.write('https://towardsdatascience.com/an-analysis-of-property-prices-in-ireland-6fc34a56ac87')
    st.write('Git Repo: https://github.com/ozwaldsux/Housing_Data.git')
    

































