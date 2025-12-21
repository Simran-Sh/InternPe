
import streamlit as st
import pickle
import pandas as pd

teams = ['Sunrisers Hyderabad',
 'Royal Challengers Bangalore',
 'Kings XI Punjab',
 'Mumbai Indians',
 'Kolkata Knight Riders',
 'Rajasthan Royals',
 'Delhi Capitals',
 'Chennai Super Kings']

city = ['Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
       'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
       'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Bengaluru', 'Indore', 'Dubai', 'Sharjah', 'Navi Mumbai',
       'Guwahati']


pipe_rf = pickle.load(open('ipl_model.pkl', 'rb'))

st.title('IPL Win Predictor')
st.write('Welcome to the IPL Win Predictor app! This application predicts the winner of an IPL match based on various input parameters.')

col_1,col2 =st.columns(2)
with col_1:
       batting_team = st.selectbox('Select the Batting team',sorted(teams)) # selectbox for batting team sorted alphabetically
with col2:
        bowling_team = st.selectbox('Select the Bowling team',sorted(teams))

selected_city = st.selectbox('City', sorted(city))
total_runs_x = st.number_input('Target Runs', min_value=0, max_value=400, value=150, step=1)

col3, col4, col5 = st.columns(3)
with col3:
         score = st.number_input('Score',min_value=0, step=1)
with col4:
         overs = st.number_input('Overs Completed (in decimal)',min_value=0.0, max_value=20.0, step=0.1)
with col5:
         wickets = st.number_input('Wickets out',min_value=0, max_value=10, step=1)   

if st.button('Predict Probability'):
    runs_left = total_runs_x - score

    # Parse overs entered as decimal (e.g. 10.2 -> 10 overs and 2 balls)
    overs_whole = int(overs)
    overs_fraction = int(round((overs - overs_whole) * 10))
    if overs_fraction >= 6:
        carry = overs_fraction // 6
        overs_whole += carry
        overs_fraction = overs_fraction % 6
    balls_bowled = overs_whole * 6 + overs_fraction
    balls_left = max(0, 120 - balls_bowled)

    wickets_left = 10 - wickets

    overs_played_decimal = overs_whole + (overs_fraction / 6)
    current_runrate = (score / overs_played_decimal) if overs_played_decimal > 0 else 0
    required_runrate = (runs_left * 6) / balls_left if balls_left > 0 else 0

    input_dict = {'batting_team':[batting_team],
                  'bowling_team':[bowling_team], 
                  'city':[selected_city],
                  'runs_left':[runs_left],
                  'balls_left':[balls_left],
                  'wickets_left':[wickets_left],
                  'total_runs_x':[total_runs_x],
                  'current_runrate':[current_runrate],
                  'required_runrate':[required_runrate]}

    input_df = pd.DataFrame(input_dict)
    st.table(input_df)
    
    result = pipe_rf.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]

    st.header('Prediction Results')
    st.subheader(f"{batting_team} has {round(win*100,2)}% chance to win the match")
    st.subheader(f"{bowling_team} has {round(loss*100,2)}% chance to win the match")

