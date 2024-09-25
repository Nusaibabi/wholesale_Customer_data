import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Wholesale customer data')





data=pd.read_csv('/workspaces/wholesale_Customer_data/mentornow/Wholesale_customers_data.csv')
with st. expander('show data'):
    st.dataframe(data)

regions=['Ahmedabad','Banglore','Chennai']

option=st.sidebar.selectbox('Select Region',[1,2,3], format_func=lambda x: regions[x-1])
df=data[data['Region']==option]


option1=st.sidebar.selectbox('Select Channel',[1,2,])
df1=df[df['Channel']==option1]
st.write(df1)

col1,col2,col3= st.columns(3)
fresh_t=df1['Fresh'].sum()

col1.metric(label='Total fresh',value=df1['Fresh'].sum())
col2.metric(label='Total Milk',value=df1['Milk'].sum())
col3.metric(label='Total Grocery',value=df1['Grocery'].sum())

col1.metric(label='Total Frozen',value=df1['Frozen'].sum())
col2.metric(label='Total Detergents & Paper',value=df1['Detergents_Paper'].sum())
col3.metric(label='Total Delicatessen',value=df1['Delicassen'].sum())

fig=px.bar(x=['Fresh','Milk','Grocery','Frozen','Detergents_Paper','Delicassen'], y=[df1['Fresh'].sum(),df1['Milk'].sum(),df1['Grocery'].sum(),df1['Frozen'].sum(),df1['Detergents_Paper'].sum(),df1['Delicassen'].sum()])
st.plotly_chart(fig)
