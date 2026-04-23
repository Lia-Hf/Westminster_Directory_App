import streamlit as st
import pandas as pd
import numpy as np
import re

st.set_page_config(page_title="WU Directory", layout="wide")

st.title('Directory at Westminster University')

st.write("This is an enhanced alternative to the employee [directory](https://westminsteru.edu/campus-directory/index.html) at Westminster University." )
#pd_version = pd.__version__
#st.write(st.__version__)
#st.write(pd_version)



data = pd.read_csv("WU_directory.csv") 

department_list = np.insert(np.sort(data['Department'].unique()), 0, 'All Departments')

department = st.selectbox(label = 'Choose one department from below:', options = department_list)

if department != 'All Departments':
    data = data.query("Department == @department")




col1, col2, col3, col4 = st.columns([0.2,0.2,0.2,0.4])
with col1:
    st.text("Type of Role:")
with col2:
    role_faculty = st.checkbox('Faculty', value=1)
with col3:
    role_staff = st.checkbox('Staff', value=1)

if not role_faculty:
    data = data.query("Role != 'Faculty'")

if not role_staff:
    data = data.query("Role != 'Staff'")




col1, col2, col3, col4 = st.columns([0.2,0.2,0.2,0.4])
with col1:
    st.text("Contract:")
with col2:
    full_time = st.checkbox('Full Time', value=1)
with col3:
    part_time = st.checkbox('Part Time', value=1)

if not full_time:
    data = data.query("Contract != 'FULL-TIME'")

if not part_time:
    data = data.query("Contract != 'PART-TIME'")




col1, col2, col3, col4, col5 = st.columns([0.2, 0.15, 0.2, 0.2, 0.2])
with col1:
    st.text("Position:")
with col2:
    professor = st.checkbox('Professor', value=1)
with col3:
    associate_professor = st.checkbox('Associate Professor', value=1)
with col4: 
    assistant_professor = st.checkbox('Assistant Professor', value=1)
with col5:
    other_pos = st.checkbox('Other', value=1) 


if not professor:
    data = data[~data["Position"].str.contains(r'^Professor', case=False, na=False)]

if not associate_professor:
    data = data[~data["Position"].str.contains("Associate Professor", case=False, na=False)]

if not assistant_professor:
    data = data[~data["Position"].str.contains("Assistant Professor", case=False, na=False)]

if not other_pos:
    prof_titles = ["Professor", "Associate Professor", "Assistant Professor"]
    data = data[data["Position"].str.contains('|'.join(prof_titles), case=False, na=False)]




search_text = st.text_input("Search Name:")

use_regex = st.checkbox("Use Regular Expression", value=False)

if search_text:
    
    if use_regex:
        data = data[data["Name"].str.contains(search_text, regex=True, na=False)]
    
    else:
        data = data[data["Name"].str.contains(search_text, case=False, regex=False, na=False)]




st.dataframe(data, hide_index=True)


