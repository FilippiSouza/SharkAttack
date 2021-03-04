import pandas as pd
import streamlit as st
import os
import numpy as np
import re

st.title('GLOBAL SHARK ATTACK')
col1_0, col2_0, col3_0 = st.beta_columns(3)

with col2_0:
    st.markdown("![Alt Text](https://media.giphy.com/media/aUs3EKOdlovgQ/giphy.gif)")
with col1_0:
    st.markdown("![Alt Text](https://media.giphy.com/media/aUs3EKOdlovgQ/giphy.gif)")
with col3_0:
    st.markdown("![Alt Text](https://media.giphy.com/media/aUs3EKOdlovgQ/giphy.gif)")

st.header('An Exploratory Analysis')
st.markdown('This document aims to demonstrate a way to clean the database provided and visuzalize some of its patterns and distributions')


path = os.path.expanduser('~/SharkAttack/')

df = pd.read_excel(path+'db_attack.xlsx')

df0 = pd.read_csv(path+'attacks.csv', encoding='latin-1')

initial_len = len(df0)
final_len = len(df)

col1, col2, col3 = st.beta_columns(3)

with col2:
    st.markdown(f'*Initial database length: {initial_len}*')
    st.markdown(f'*Final database length: {final_len}*')
    st.write('\n')


#FILTERING

#YEAR
adbc = st.sidebar.selectbox('WAS CHRIST ALIVE?', ['B.C.','A.D.'], 1)
years = list(df[df['ad/bc'] == adbc].index)
years = df.loc[years,'year_avg']
years = [year for year in years if year != 'unknow']
fst_year = min(years)
last_year = max(years)
anos = st.sidebar.slider('PERIOD',fst_year,last_year,(fst_year,last_year))
valid_years = df[df['year_avg']!='unknow'].index
valid_years = list(valid_years)
df_filtered = df.loc[valid_years]
filt_year  = (df_filtered['year_avg']>=min(anos)) & (df_filtered['year_avg']<=max(anos))


#BODY PART INJURY
body =st.sidebar.text_input('A HAND FOR YOUR LIFE?')
if body is np.nan:
    pass
else:
    losses = df[df['injury_kw'].apply(lambda x: body in x) == True].index
    losses = [loss for loss in losses if loss in valid_years]
    df_filtered = df_filtered.loc[losses,]






##TOTAL CASES
st.subheader('REPORTED ATTACKS THROUGH THE YEARS')
df_filtered = df_filtered[filt_year]
total_cases = len(df_filtered)
col1_2, col2_2, col3_2 = st.beta_columns(3)
with col3_2:
        st.markdown(f'Total number of cases: **{total_cases}**')
cases_year = df_filtered['year_avg'].value_counts()
st.area_chart(cases_year)
df_filtered[['date','area','injury','species']]

#ACTIVITY
st.subheader('20 ACTIVITIES MOST OFTEN PRACTICED DURING AN ATTACK')
unknow = round(
    len(df_filtered[df_filtered['act_cat'] =='unknow'])/len(df),1)*100
col1_3, col2_3, col3_3 = st.beta_columns(3)
with col3_3:
    st.markdown(f'Unknow: **{unknow}%**')
df_filtered_filt = df_filtered[df_filtered['act_cat'] != 'unknow']
cases_activity = df_filtered_filt['act_cat'].value_counts(normalize=True).nlargest(20)
st.bar_chart(cases_activity)

#SIZE
st.subheader('FREQUENCY BY SHARK SIZE')
unknow = round(
    len(df_filtered[df_filtered['shark_size'] == 'unknow'])/len(df),1)*100
col1_4, col2_4, col3_4 = st.beta_columns(3)
with col3_4:
    st.markdown(f'Unknow: **{unknow}%**')
df_filtered_filt = df_filtered[df_filtered['shark_size']!='unknow']
size = df_filtered_filt['shark_size'].value_counts(normalize=True).nlargest(20)

st.bar_chart(size)

#INJURY
st.subheader('MOST COMMOM INJURIES')
df_l = df_filtered[df_filtered['short_injury'].str.contains('left')]
df_r = df_filtered[df_filtered['short_injury'].str.contains('right')]
l_cases = len(df_l)
r_cases = len(df_r)
injury = df_filtered['short_injury'].value_counts().nlargest(20)
registers = injury.sum()
col1_5, col2_5, = st.beta_columns(2)
with col2_5:
    st.markdown(f'Cases Reported: **{registers}**')
    st.markdown(f'Right side affected: **{round(r_cases/(l_cases+r_cases),1)*100}%**')
    st.markdown(f'Left side affected: **{round(l_cases / (l_cases + r_cases),1)*100}%**')
    not_confirmed = len(df_filtered[df_filtered['species'] == 'shark involvement not confirmed'])
    no_shark = len(df_filtered[df_filtered['species']=='no shark involvement'])
    len(df_filtered[df_filtered['species'] == 'shark involvement not confirmed'])
    st.markdown(f'Shark involvement not confirmed: **{not_confirmed}**')
    st.markdown(f'No shark involved: **{no_shark}**')

with col1_5:
    injury


len(df_filtered[df_filtered['species']=='shark involvement not confirmed'])
