import pandas as pd
import numpy as np

ipl_matches='https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv'
matches=pd.read_csv(ipl_matches)


def teamsAPI():
  teams=list(set(list(matches['Team1'])+list(matches['Team2'])))
  teams_dict={
    'teams':teams
  }
  return teams_dict

def team_vs_team(team1,team2):
  valid_teams=list(set(list(matches['Team1'])+list(matches['Team2'])))
  
  if team1 in valid_teams and team2 in valid_teams:
    temp_df=matches[(matches['Team1']==team1) & (matches['Team2']==team2) | (matches['Team1']==team2) & (matches['Team2']==team1)]
    total_matches=temp_df.shape[0]

    matches_won_team1=temp_df['WinningTeam'].value_counts()[team1]
    matches_won_team2=temp_df['WinningTeam'].value_counts()[team2]
    draws=total_matches-(matches_won_team1+matches_won_team2)

    response={
        'total_matches':str(total_matches),
        team1:str(matches_won_team1),
        team2:str(matches_won_team2),
        'draws':str(draws)
      }
    return response
  else:
    return {'message':'Invalid team name'}
  

def players():
  Team1Players=list(set([j for i in matches['Team1Players'] for j in list(i[1:-1].split(','))]))
  Team2Players=list(set([j for i in matches['Team2Players'] for j in list(i[1:-1].split(','))]))
  players=Team1Players+Team2Players
  players=list(set(map(lambda player:player.split("'")[1],players)))
  players_dict={
    'players':sorted(players),
    'total':len(players)
  }
  return players_dict

def allRecord(team):
    df = matches[(matches['Team1'] == team) | (matches['Team2'] == team)].copy()
    mp = df.shape[0]
    won = df[df.WinningTeam == team].shape[0]
    nr = df[df.WinningTeam.isnull()].shape[0]
    loss = mp - won - nr
    nt = df[(df.MatchNumber == 'Final') & (df.WinningTeam == team)].shape[0]
    return {'matchesplayed': mp,
            'won': won,
            'loss': loss,
            'noResult': nr,
            'title': nt}
