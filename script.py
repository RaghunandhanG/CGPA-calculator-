import streamlit as st

st.title('CGPA CALCI')

no_of_sub = st.number_input("Select the number of Subjects....", value=1, placeholder="Type a number..." , step = 1)
total_credits = 0
total = 0


if no_of_sub is not None:
    for i in range(int(no_of_sub)):
        
        credits = st.slider(f':blue[Credits of the Subject {i+1}]', 1, 4)
        grade_pts = st.slider(f'Grade points of the Subject {i+1}', 6, 10)
        
        
        total_credits += credits
        total += credits * grade_pts
        
        
    cgpa = total / total_credits

    col1, col2 = st.columns(2)
    col1.metric(label="CGPA", value=round(cgpa , 2) )
    col2.metric(label="Total Credits", value = total_credits)
    
