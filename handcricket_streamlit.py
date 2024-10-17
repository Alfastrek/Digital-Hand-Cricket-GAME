import random
import pandas as pd
import numpy as np
import streamlit as st

# Initialize game parameters
st.title('Hand Cricket Game')
gamepl = ['BAT', 'BALL']
poss = (0, 1, 2, 3, 4, 5, 6)  # Runs Allowed

# Initialize session state
if 'userteamtotalruns' not in st.session_state:
    st.session_state.userteamtotalruns = 0
if 'compteamtotalruns' not in st.session_state:
    st.session_state.compteamtotalruns = 0
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
if 'current_round' not in st.session_state:
    st.session_state.current_round = 0
if 'oddeve' not in st.session_state:  # Initialize oddeve
    st.session_state.oddeve = None
if 'oeresult' not in st.session_state:  # Initialize oeresult
    st.session_state.oeresult = None

# Function for odd-even game
def oddevengame():
    oddeve = st.selectbox("Choose ODD or EVEN", ["ODD", "EVEN"], key="oddeve_choice")
    oeno = st.number_input("Choose your number (within 0 to 6):", 0, 6, key="oeno")
    if st.button("Submit ODD/EVEN"):
        rand = np.random.choice(poss)
        oeresult = oeno + rand  # Total result of odd-even game
        st.session_state.oeresult = oeresult
        st.session_state.oddeve = oddeve  # Save to session state after submission
        st.write(f"Computer Chooses: {rand} \nAnd the Total makes: {oeresult}")

# Function for batting
def batting(User_team):
    userrecord = np.array([])
    for user in User_team:
        runs = st.number_input(f'{user}, Play Runs (0-6):', 0, 6, key=f'runs_{user}')
        if runs not in poss:
            st.write("Sorry, you are out! Only 0 to 6 is the range for runs.")
            break
        rand1 = np.random.choice(poss)
        st.write(f"Computer Chooses: {rand1}")
        
        if rand1 == runs:
            st.write(f"{user} is OUT!\n")
            break
        else:
            userrecord = np.append(userrecord, runs)
            st.write(f"Your Runs after this round are: {userrecord}")
            st.session_state.userteamtotalruns += runs
            
    return st.session_state.userteamtotalruns

# Function for bowling
def balling(Comp_team):
    compteamtotalruns = 0
    for comp in Comp_team:
        balls = st.number_input(f'{comp}, Enter your Bowling input (0-6):', 0, 6, key=f'balls_{comp}')
        if balls not in poss:
            st.write("Sorry, you are out! Only 0 to 6 is the range for runs.")
            break
        rand2 = np.random.choice(poss)
        st.write(f"{comp} Chooses: {rand2}")
        
        if rand2 == balls:
            st.write(f"You Win!\nThe {comp} is OUT!")
            break
        else:
            compteamtotalruns += rand2
            st.write(f"Computer Runs after this ball is: {rand2}")

    st.session_state.compteamtotalruns += compteamtotalruns
    return st.session_state.compteamtotalruns

# Function for final overview
def final_overview():
    st.write("\nTOTAL RUNS OF USER TEAM:", st.session_state.userteamtotalruns)
    st.write("TOTAL RUNS OF COMPUTER TEAM:", st.session_state.compteamtotalruns)
    if st.session_state.userteamtotalruns > st.session_state.compteamtotalruns:
        st.write("\nYOU WON!!!! 🎉")
    elif st.session_state.userteamtotalruns < st.session_state.compteamtotalruns:
        st.write("\nYOU LOSE!!! 😢")
    else:
        st.write("\nIt's A DRAW. 🤝")
        st.write("THANK YOU FOR PLAYING!")

# Define the main game function
def maingame():
    if st.session_state.current_round == 0:
        Players = st.number_input("Enter Total Players on each side:", 1, 10, key="players")
        User_team = [st.text_input(f"Enter Name of Player {i+1}:", key=f'player_{i}') for i in range(Players)]
        
        Comp_team = [f"ROBO-{i + 1}" for i in range(Players)]  # Comp team names
        if st.button("Start Game"):
            st.session_state.game_started = True
            st.session_state.User_team = User_team
            st.session_state.Comp_team = Comp_team
            st.session_state.current_round += 1
    
    elif st.session_state.current_round == 1:
        st.write("Overview of the TEAMS:")
        data = {
            "USER TEAM": st.session_state.User_team,
            "COMP TEAM": st.session_state.Comp_team
        }
        sr_no = [i + 1 for i in range(len(st.session_state.User_team))]
        df = pd.DataFrame(data, index=sr_no)
        st.write(df)

        oddevengame()
        st.session_state.current_round += 1
    
    elif st.session_state.current_round == 2:
        if (st.session_state.oddeve == 'EVEN' and st.session_state.oeresult % 2 == 0) or (st.session_state.oddeve == "ODD" and st.session_state.oeresult % 2 != 0):
            st.write("User won the ODD/EVEN Toss!")
            Choice = st.selectbox("Choose BAT OR BALL", ["BAT", "BALL"], key="choice")
            
            if Choice == 'BAT':
                batting(st.session_state.User_team)
                st.write("Now it's your turn to Bowl!")
                balling(st.session_state.Comp_team)
                final_overview()
                st.session_state.current_round += 1
            elif Choice == "BALL":
                balling(st.session_state.Comp_team)
                st.write("Now it's your turn to Bat!")
                batting(st.session_state.User_team)
                final_overview()
                st.session_state.current_round += 1
    
        elif (st.session_state.oddeve == "ODD" and st.session_state.oeresult % 2 == 0) or (st.session_state.oddeve == "EVEN" and st.session_state.oeresult % 2 != 0):
            st.write("Computer won the ODD/EVEN Toss!")
            Choice1 = random.choice(gamepl)
            st.write("\nComputer chooses to:", Choice1)
            
            if Choice1 == 'BAT':
                balling(st.session_state.Comp_team)
                st.write("Now it's your turn to Bat!")
                batting(st.session_state.User_team)
                final_overview()
                st.session_state.current_round += 1
            elif Choice1 == "BALL":
                batting(st.session_state.User_team)
                st.write("Now it's your turn to Bowl!")
                balling(st.session_state.Comp_team)
                final_overview()
                st.session_state.current_round += 1

# Run the main game function
if __name__ == "__main__":
    maingame()
